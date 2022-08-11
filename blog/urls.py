from django.urls import path
from . import views
from django.conf import settings
# import debug_toolbar
app_name="blog"
urlpatterns = [
    # path('', views.index, name='index'),
    
    path('', views.IndexView.as_view(), name='index'),

    path('archives/', views.ArchivesView.as_view(),name='archives'),
    path('post/<int:pk>', views.article, name='article'),
    #path('post/', views.myview, name='myview'),

    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('categories/', views.Categories.as_view(), name='categories'),

    path('tags/', views.TagsView.as_view(),name='tags'),
    path('tag_list/<int:pk>', views.TagListView.as_view(), name='tag_list'),

    path('books/', views.BooksView.as_view(), name='books'),
    path('book_detail/<int:pk>', views.book_detail, name='book_detail'),
    path('book_list/<int:pk>', views.BookListView.as_view(), name='book_list'),

    path('movies/', views.MoviesView.as_view(), name ='movies' ),
    path('movie_detail/<int:pk>', views.movie_detail, name='movie_detail'),
    path('movie_list/<int:pk>', views.MovieListView.as_view(), name='movie_list'),

    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),

    path('messages/',views.messages,name='messages'),

    path('courses/',views.CoursesView.as_view(),name='courses'),
    path('course/<int:pk>',views.course,name='course'),

]
