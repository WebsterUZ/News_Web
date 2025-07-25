from django.urls import path

from news.views import news_list_view, news_detail_view, add_news_view, category_view

urlpatterns = [
    path('', news_list_view, name='home'),
    path('news/add/', add_news_view, name='add_news'),
    path('news/<int:pk>/', news_detail_view, name='news_detail'),
    path('category/<int:category_id>/', category_view, name='category_view'),  # <-- YANGI
]
