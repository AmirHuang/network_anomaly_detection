# Generated by Django 2.1.2 on 2019-03-27 17:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nt_user', '0002_auto_20190326_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedbackmessage',
            name='id',
            field=models.CharField(default=uuid.UUID('27d15d92-5d29-4975-9998-4c4810eaca9d'), editable=False, max_length=40, primary_key=True, serialize=False),
        ),
    ]