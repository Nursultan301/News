from django.shortcuts import render, get_object_or_404, redirectfrom django.views.generic import ListView, DetailView, CreateViewfrom django.urls import reverse_lazyfrom django.contrib.auth.mixins import LoginRequiredMixinfrom django.core.paginator import Paginatorfrom .models import News, Categoryfrom .forms import NewsFormfrom .utils import MyMixin## def test(request):#     objects = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ]#     paginator = Paginator(objects, 2)#     page_num = request.GET.get('page', 1)#     page_objects = paginator.get_page(page_num)#     return render(request, 'news/pagin_test.html', {'page_obj': page_objects})class HomeNews(MyMixin, ListView):  # context_object_name  по умолчанию object_list #    """ Список новостей """    model = News    template_name = 'news/home_news_list.html'    context_object_name = 'news'    paginate_by = 1    # mixin_prop = 'hello world'    # extra_context = {'title': 'Главная'}    def get_context_data(self, *, object_list=None, **kwargs):        context = super().get_context_data(**kwargs)        context['title'] = 'Главная страница'        context['news_count'] = News.objects.filter(is_published=True)        # context['mixin_prop'] = self.get_prop()        return context    def get_queryset(self):        return News.objects.filter(is_published=True).select_related('category')## def index(request):#     """ Список новостей """#     news = News.objects.filter(is_published=True)#     context = {#         'title': 'Список новостей',#         'news': news,#     }#     return render(request, 'news/index.html', context=context)class NewsByCategory(MyMixin, ListView):  # context_object_name  по умолчанию object_list #    """ Список категори """    model = News    template_name = 'news/category.html'    context_object_name = 'news'    allow_empty = False    paginate_by = 2    def get_context_data(self, *, object_list=None, **kwargs):        context = super().get_context_data(**kwargs)        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])        return context    def get_queryset(self):        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')# def get_category(request, category_id):#     """ Список категори """#     news = News.objects.filter(category_id=category_id)#     # category = Category.objects.get(pk=category_id)#     category = get_object_or_404(Category, pk=category_id)#     context = {#         'title': 'Список новостей',#         'news': news,#         'category': category,#     }#     return render(request, 'news/category.html', context=context)class ViewNews(DetailView):  # context_object_name  по умолчанию object #    """ Просмотр новостей """    model = News    context_object_name = 'news_item'    # template_name = "news/news_detail.html"    # pk_url_kwarg = 'news_id'## def view_news(request, news_id):#     """ Просмотр новостей """#     # news_item = News.objects.get(pk=news_id)#     news_item = get_object_or_404(News, pk=news_id)#     return render(request, 'news/view_news.html', {"news_item": news_item})class CreateNews(LoginRequiredMixin, CreateView):    """ Добавление новости """    form_class = NewsForm    template_name = 'news/add_news.html'    # success_url = reverse_lazy('home')    # login_url = '/admin/'    raise_exception = True# def add_news(request):#     """ Добавление новости """#     if request.method == 'POST':#         form = NewsForm(request.POST)#         if form.is_valid():#             # print(form.cleaned_data)#             # news = News.objects.create(**form.cleaned_data)#             news = form.save()#             return redirect(news)#     else:#         form = NewsForm()#     return render(request, 'news/add_news.html', {"form": form})#