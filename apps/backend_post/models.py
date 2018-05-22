from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.
class Articles(models.Model):
    author = models.CharField(max_length=10,default='zjh')
    title = models.CharField(max_length=20,unique=True)
    content = MarkdownxField()
    create_date = models.DateTimeField(auto_now_add=True)
    editor_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<{}:{}>'.format(self.author,self.title)
    class Meta:
        db_table = 'article'

