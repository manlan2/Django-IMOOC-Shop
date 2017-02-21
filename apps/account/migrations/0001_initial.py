# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-14 11:17
from __future__ import unicode_literals

import datetime
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(default='New', max_length=10, verbose_name='\u6635\u79f0')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('gender', models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='male', max_length=5, verbose_name='\u6027\u522b')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4f4f\u5740')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='\u7535\u8bdd')),
                ('image', models.ImageField(upload_to='image/superuser/%Y/%m', verbose_name='\u5934\u50cf')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '\u8d85\u7ea7\u7528\u6237',
                'verbose_name_plural': '\u8d85\u7ea7\u7528\u6237',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=10, verbose_name='\u5bc6\u7801')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
                ('sex', models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], default='male', max_length=5)),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='\u624b\u673a')),
                ('learn_time', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u65f6\u957f')),
                ('experience', models.IntegerField(default=0, verbose_name='\u7ecf\u9a8c')),
                ('image', models.ImageField(default='', upload_to='image/user/%Y/%m', verbose_name='\u5934\u50cf')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='QQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=10, verbose_name='\u6635\u79f0')),
                ('password', models.CharField(max_length=10, verbose_name='\u5bc6\u7801')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
                ('image', models.ImageField(upload_to='image/qq/%Y/%m', verbose_name='\u5934\u50cf')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Account', verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': 'QQ',
                'verbose_name_plural': 'QQ',
            },
        ),
        migrations.CreateModel(
            name='Sina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='\u6635\u79f0')),
                ('password', models.CharField(max_length=10, verbose_name='\u5bc6\u7801')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
                ('image', models.ImageField(upload_to='image/sina/%Y/%m', verbose_name='\u5934\u50cf')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Account', verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u65b0\u6d6a',
                'verbose_name_plural': '\u65b0\u6d6a',
            },
        ),
        migrations.CreateModel(
            name='WeChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='\u6635\u79f0')),
                ('password', models.CharField(max_length=10, verbose_name='\u5bc6\u7801')),
                ('image', models.ImageField(upload_to='image/wechat/%Y/%m', verbose_name='\u5934\u50cf')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Account', verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1',
                'verbose_name_plural': '\u5fae\u4fe1',
            },
        ),
    ]
