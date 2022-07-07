from django.shortcuts import render, get_object_or_404, reverse
from .models import Article
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .forms import ArticleModelForm

# Create your views here.


class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()
    # def get(self, request):
    #     # <view logic>
    #     return render(request, self.template_name, context={"queryset": self.queryset})


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = "articles/article_update.html"
    form_class = ArticleModelForm
    # queryset = Article.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')


