# Generated by Django 2.0.8 on 2022-08-09 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='书名')),
                ('author', models.CharField(max_length=100, verbose_name='作者')),
                ('cover', models.ImageField(blank=True, upload_to='books', verbose_name='封面图')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='豆瓣评分')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='标题')),
                ('detail', mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='读书笔记')),
                ('created_time', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='添加时间')),
                ('time_consuming', models.CharField(max_length=100, verbose_name='阅读初始时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('words', models.PositiveIntegerField(default=0, verbose_name='字数')),
                ('excerpt', models.CharField(blank=True, max_length=300, verbose_name='摘要')),
            ],
            options={
                'verbose_name': '我的书单',
                'verbose_name_plural': '我的书单',
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '图书分类',
                'verbose_name_plural': '图书分类',
            },
        ),
        migrations.CreateModel(
            name='BookTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签')),
            ],
            options={
                'verbose_name': '书籍标签',
                'verbose_name_plural': '书籍标签',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类目录',
                'verbose_name_plural': '分类目录',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='教程名称')),
                ('cover', models.ImageField(blank=True, upload_to='course', verbose_name='上传封面')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('category', models.CharField(max_length=100, verbose_name='教程分类')),
                ('introduce', models.CharField(blank=True, max_length=200, verbose_name='教程简介')),
                ('status', models.CharField(max_length=50, verbose_name='更新状态')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='创建时间')),
                ('comments', models.PositiveIntegerField(default=0, verbose_name='评论数')),
                ('numbers', models.PositiveIntegerField(default=0, verbose_name='教程数量')),
                ('author', models.ForeignKey(default='reborn', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '教程列表',
                'verbose_name_plural': '教程列表',
            },
        ),
        migrations.CreateModel(
            name='MeanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='菜单名称')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单链接')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单图标')),
            ],
            options={
                'verbose_name': '菜单栏',
                'verbose_name_plural': '菜单栏',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='给我留言')),
            ],
            options={
                'verbose_name': '网站留言',
                'verbose_name_plural': '网站留言',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='电影名称')),
                ('director', models.CharField(max_length=100, verbose_name='导演')),
                ('actor', models.CharField(max_length=100, verbose_name='主演')),
                ('cover', models.ImageField(blank=True, upload_to='movies', verbose_name='上传封面')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='豆瓣评分')),
                ('release_time', models.DateField(verbose_name='上映时间')),
                ('created_time', models.DateField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('length_time', models.PositiveIntegerField(default=0, verbose_name='电影时长')),
                ('watch_time', models.DateField(default=django.utils.timezone.now, verbose_name='观看时间')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='标题')),
                ('detail', mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='观影后感')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('words', models.PositiveIntegerField(default=0, verbose_name='字数')),
                ('excerpt', models.CharField(blank=True, max_length=300, verbose_name='摘要')),
            ],
            options={
                'verbose_name': '我的影单',
                'verbose_name_plural': '我的影单',
            },
        ),
        migrations.CreateModel(
            name='MovieCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='电影分类')),
            ],
            options={
                'verbose_name': '电影分类',
                'verbose_name_plural': '电影分类',
            },
        ),
        migrations.CreateModel(
            name='MovieTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '电影标签',
                'verbose_name_plural': '电影标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='标题')),
                ('body', mdeditor.fields.MDTextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('excerpt', models.CharField(blank=True, max_length=300, verbose_name='摘要')),
                ('views', models.PositiveIntegerField(default=0)),
                ('words', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(default='reborn', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='文章分类')),
            ],
            options={
                'verbose_name': '文章列表',
                'verbose_name_plural': '文章列表',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '标签列表',
                'verbose_name_plural': '标签列表',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签类型'),
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.MovieCategory', verbose_name='电影分类'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tag',
            field=models.ManyToManyField(to='blog.MovieTag', verbose_name='电影标签'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BookCategory', verbose_name='书籍分类'),
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(to='blog.BookTag', verbose_name='本书标签'),
        ),
    ]
