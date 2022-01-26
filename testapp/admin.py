from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Rubric, Article

admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category')


# admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(Article, ArticleAdmin)

