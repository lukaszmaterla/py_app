from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
)
# Create your views here.
from .models import Article
from .forms import ArticleModelForm


class ArticleListView(ListView):
    template_name = 'blog/some.html' # override basic view
    queryset = Article.objects.all() # blog/<modelname>_list.html


class ArticleDetailView(DetailView):
    # queryset = Article.objects.all() # blog/<modelname>_list.html

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all() # blog/<modelname>_list.html
    form_class = ArticleModelForm
