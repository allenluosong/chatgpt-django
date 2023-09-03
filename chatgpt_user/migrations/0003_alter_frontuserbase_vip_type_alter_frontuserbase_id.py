# Generated by Django 4.2.4 on 2023-09-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_user', '0002_rename_customer_id_frontuserbase_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontuserbase',
            name='VIP_TYPE',
            field=models.IntegerField(choices=[('0', '普通用户'), ('1', 'vip付费用户')], default='0', help_text='用户类型', verbose_name='Status (*)'),
        ),
        migrations.AlterField(
            model_name='frontuserbase',
            name='id',
            field=models.AutoField(help_text='客户唯一编号', primary_key=True, serialize=False, unique=True, verbose_name='客户唯一编号'),
        ),
    ]
