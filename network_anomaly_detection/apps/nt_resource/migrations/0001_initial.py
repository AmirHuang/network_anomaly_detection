# Generated by Django 2.1.2 on 2019-03-28 10:40

from django.db import migrations, models
import nt_core.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatNormalResource',
            fields=[
                ('id', models.CharField(default=uuid.UUID('dfdfb81a-7aba-464d-af2a-47820eef2359'), editable=False, max_length=40, primary_key=True, serialize=False)),
                ('create_time', models.BigIntegerField(default=nt_core.models.get_current_time_bigint)),
                ('update_time', models.BigIntegerField(default=nt_core.models.get_current_time_bigint)),
                ('appid', models.IntegerField(blank=True, null=True)),
                ('response_time', models.FloatField(blank=True, null=True)),
                ('request_count', models.IntegerField(blank=True, null=True)),
                ('fail_count', models.IntegerField(blank=True, null=True)),
                ('click_num', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'cat_normal_resource',
            },
        ),
    ]
