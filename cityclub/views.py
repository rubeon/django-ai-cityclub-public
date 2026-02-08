from django.views.generic import ListView, DetailView
from .models import Reporter, Article

class ReporterListView(ListView):
    model = Reporter
    template_name = 'cityclub/reporter_list.html'

class ReporterDetailView(DetailView):
    model = Reporter
    template_name = 'cityclub/reporter_detail.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'cityclub/article_list.html'
    ordering = ['-pub_date']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'cityclub/article_detail.html'