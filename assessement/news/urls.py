from django.urls import path
from news.views.RetrieveNewsAPIView import RetrieveNewsAPIView


from news.views.NewsByCategoryAPIView import NewsByCategoryAPIView

from news.views.NewsByCountryAPIView import NewsByCountryAPIView
from news.views.NewsByQueryAPIView import NewsByQueryAPIView
from news.views.NewsBySourceAPIView import NewsBySourceAPIView

from django.views.decorators.cache import cache_page

urlpatterns = [
    path('news/country', NewsByCountryAPIView.as_view(), name='news-by-country'),
    path('news/category', NewsByCategoryAPIView.as_view(), name='news-by-category'),
    path('news/source', NewsBySourceAPIView.as_view(), name='news-by-source'),
    path('news/query', NewsByQueryAPIView.as_view(), name='news-by-query'),
    path('news/', RetrieveNewsAPIView.as_view(), name='get-news'),
    
    
    
    
]
    
