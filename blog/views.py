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


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() # <blog>/<modelname>_list.html
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() # <blog>/<modelname>_list.html

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class ArticleListView(ListView):
    template_name = 'blog/some.html' # override basic view
    queryset = Article.objects.all() # blog/<modelname>_list.html


class ArticleDetailView(DetailView):
    # queryset = Article.objects.all() # blog/<modelname>_list.html

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


