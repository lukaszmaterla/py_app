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


class ArticleListView(ListView):
    template_name = 'blog/some.html' # override basic view
    queryset = Article.objects.all() # blog/<modelname>_list.html


class ArticleDetailView(DetailView):
    queryset = Article.objects.all() # blog/<modelname>_list.html

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)