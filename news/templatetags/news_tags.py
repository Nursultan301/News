from django import template
from django.db.models import Count, F
from django.core.cache import cache

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg='Inclusion tag'):
    categories = cache.get('categories')
    # if not categories:
    #     categories = Category.objects.annotate(cnt=Count('category', filter=F('category__is_published'))).filter(cnt__gt=0,)
    #     cache.set('categories', categories, 20)
    categories = Category.objects.annotate(cnt=Count('category', filter=F('category__is_published'))).filter(
        cnt__gt=0, )
    return {"categories": categories, 'arg': arg}
