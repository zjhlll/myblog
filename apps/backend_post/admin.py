from django.contrib import admin
from .models import Articles,Category,Person_tags
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
admin.site.register(Articles,MarkdownxModelAdmin)
admin.site.register(Category)
admin.site.register(Person_tags)