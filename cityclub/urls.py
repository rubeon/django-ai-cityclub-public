from django.urls import path
from .views import ReporterListView, ReporterDetailView, ArticleListView, ArticleDetailView

urlpatterns = [
    path('reporters/', ReporterListView.as_view(), name='reporter-list'),
    path('reporters/<int:pk>/', ReporterDetailView.as_view(), name='reporter-detail'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]