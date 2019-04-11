from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)
# Create your views here.
from .models import Article


class ArticleListView(ListView):
    template_name = 'blog/some.html' # override basic view
    queryset = Article.objects.all() # blog/<modelname>_list.html