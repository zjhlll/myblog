from django.contrib import admin
from .models import Articles
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.
admin.site.register(Articles,MarkdownxModelAdmin)