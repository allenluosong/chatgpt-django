# Generated by Django 4.2.4 on 2023-09-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_user', '0004_frontuserbase_call_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontuserbase',
            name='username',
            field=models.EmailField(blank=True, help_text='登录邮箱', max_length=255, null=True, unique=True, verbose_name='登录邮箱'),
        ),
    ]
