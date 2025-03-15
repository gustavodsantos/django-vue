from django.contrib import admin
from django_min_custom_user.admin import MinUserAdmin
from ordered_model.admin import OrderedModelAdmin

from djavue.cursos.models import Curso, User


@admin.register(User)
class UserAdmin(MinUserAdmin):
    pass


@admin.register(Curso)
class CursoAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'slug', 'descricao', 'order', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'descricao')
    list_filter = ('titulo',)
    ordering = ['order', 'titulo']
