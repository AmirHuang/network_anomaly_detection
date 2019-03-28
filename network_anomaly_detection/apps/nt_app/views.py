# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from nt_core.exceptions import RsError

from nt_app.models import CatResource
from nt_app.serializers import (
    CatResourceCreateSerializer,
    CatResourceListSerializer)


class CatResourceView(APIView):
    def post(self, request):
        req_data = request.data
        serializer = CatResourceCreateSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        cat_obj = CatResource.objects.create(**data)
        return Response({'id': cat_obj.id})

    def get(self, request):
        req_data = request.GET
        print(req_data)
        _id = req_data.get('id')
        if not _id:
            raise RsError('id不可缺少')
        cat_obj = CatResource.objects.filter(id=_id).first()
        if not cat_obj:
            raise RsError('数据不存在')
        ser_data = CatResourceListSerializer(cat_obj).data
        return Response(ser_data)

    def put(self, request):
        req_data = request.data
        print(req_data)
        _id = req_data.get('id')
        if not _id:
            raise RsError('id不可缺少')
        cat_obj = CatResource.objects.filter(id=_id).first()
        if not cat_obj:
            raise RsError("id不存在")
        ser = CatResourceListSerializer(cat_obj, req_data, partial=True)
        if ser.is_valid():
            ser.save()
        else:
            raise RsError(ser.errors)
        return Response({"result": True, "id": _id})

    def delete(self, request):
        req_data = request.data
        id = req_data.get('id')
        if id:
            try:
                obj = CatResource.objects.get(id=id)
                obj.delete()
            except Exception as e:
                raise RsError('不存在')
        else:
            raise RsError('id不可缺少')
        return Response({"result": True, "rows": id})


class CatResourceListView(ListAPIView):
    cat_search_fields = [
        'appid', 'id', 'response_time', 'request_count',
        'start_time', 'end_time', 'fail_count'
    ]
    queryset = CatResource.objects.all()
    serializer_class = CatResourceListSerializer

    def list(self, request, *args, **kwargs):
        filters = self.generate_filter(request)
        cat_lists = CatResource.objects.filter(**filters).order_by('-update_time')
        page_data = self.paginate_queryset(cat_lists)
        if page_data is not None:
            serializer = self.serializer_class(page_data, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(cat_lists, many=True)
        return Response(serializer.data)



    # def list(self, request, *args, **kwargs):
    #     #     queryset = self.filter_queryset(self.get_queryset())
    #     #
    #     #     page = self.paginate_queryset(queryset)
    #     #     if page is not None:
    #     #         serializer = self.get_serializer(page, many=True)
    #     #         return self.get_paginated_response(serializer.data)
    #     #
    #     #     serializer = self.get_serializer(queryset, many=True)
    #     #     return Response(serializer.data)

    def generate_filter(self, request):
        req_data = request.GET
        filters = {}
        for filed in self.cat_search_fields:
            field_val = req_data.get(filed)
            if field_val:
                if filed in ['id', 'appid']:
                    filters[filed] = field_val
                elif filed in ['start_time']:
                    filters['create_time__gt'] = field_val
                elif filed in ['end_time']:
                    filters['end_time__lt'] = field_val
                elif filed in ['response_time', 'request_count', 'fail_count']:
                    filters['{}__gte'.format(filed)] = field_val
                    filters['{}__lte'.format(filed)] = field_val

        return filters