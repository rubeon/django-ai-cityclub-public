from django.urls import path
from .views import ReporterListView, ReporterDetailView, ArticleListView, ArticleDetailView

urlpatterns = [
    path('reporters/', ReporterListView.as_view(), name='reporter-list'),
    path('reporters/&lt;int:pk&gt;/', ReporterDetailView.as_view(), name='reporter-detail'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/&lt;int:pk&gt;/', ArticleDetailView.as_view(), name='article-detail'),
]