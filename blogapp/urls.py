from django.urls import path
from .views import blog_main_page

app_name = 'blog'

urlpatterns = [
    path('', blog_main_page, name='blog_main_page'),
]
