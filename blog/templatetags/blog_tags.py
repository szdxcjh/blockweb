from ..models import *
from django import template
from django.db.models import Count
from comment.models import Comment
from comment.form import CommentForm
from django.contrib.contenttypes.models import ContentType

register = template.Library()

# 返回文章总量
@register.simple_tag
def get_total_posts():
    posts_number = Post.objects.all().count()
    return posts_number

# 返回文章分类总量
@register.simple_tag
def get_total_categories():
    category_number = Category.objects.all().count()
    return category_number

# 返回文章标签总量
@register.simple_tag
def get_total_tags():
    tags_number = Tag.objects.all().count()
    return tags_number

# 获取书籍数量
@register.simple_tag
def get_total_books():
    books_number = Book.objects.all().count()
    return books_number

@register.simple_tag
def base_url():
    base_url = 'http://www.eastnotes.com'
    return base_url

# 获取文章标签
@register.simple_tag
def get_posts_tags():
    tags = Tag.objects.annotate(posts_count=Count('post')).order_by('-posts_count')
    return tags

# 获取书籍标签
@register.simple_tag
def get_books_tags():
    tags = BookTag.objects.annotate(books_count=Count('book')).order_by('-books_count')
    return tags

# 获取电影数量
@register.simple_tag
def get_total_movies():
    books_number = Movie.objects.all().count()
    return books_number

# 获取电影标签
@register.simple_tag
def get_movies_tags():
    tags = MovieTag.objects.annotate(movies_count=Count('movie')).order_by('-movies_count')
    return tags

# 返回评论数量
@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type,object_id=obj.id).count()

# 返回评论表单
@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    form = CommentForm(initial={'content_type':content_type.model,'object_id':obj.pk,'reply_comment_id':'0'})
    return form

# 返回评论表
@register.simple_tag
def get_comments_list(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.id, parent=None).order_by('-comment_time')  # 获取所有与此类型相同的评论
    return comments

@register.simple_tag
def get_meanList():
    means = MeanList.objects.all().order_by('pk')
    return means

@register.simple_tag
def get_category():
    categories = Category.objects.all()
    return  categories