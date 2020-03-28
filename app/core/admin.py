from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (_('Personal Info'), {'fields': ('name',)}),
    (
        _('Permissions'),
        {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }
    ),
    (_('Important dates'), {'fields': ('last_login',)}),)
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2')
    }),
)


class RecipeAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'is_published','description',)
  list_display_links = ('id', 'name')
  list_filter = ('user',)
  list_editable = ('is_published',)
  search_fields = ('name', 'description',)
  list_per_page = 25


admin.site.register(models.User, UserAdmin)

admin.site.register(models.AggregateRating)
admin.site.register(models.RecipeCategory)
admin.site.register(models.Ingredient)
admin.site.register(models.Recipe, RecipeAdmin)


