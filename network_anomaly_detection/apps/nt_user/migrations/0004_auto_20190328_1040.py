# Generated by Django 2.1.2 on 2019-03-28 10:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nt_user', '0003_auto_20190327_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedbackmessage',
            name='id',
            field=models.CharField(default=uuid.UUID('dfdfb81a-7aba-464d-af2a-47820eef2359'), editable=False, max_length=40, primary_key=True, serialize=False),
        ),
    ]
