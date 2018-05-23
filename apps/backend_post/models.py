from django.db import models
from markdownx.models import MarkdownxField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16, verbose_name='分类名称')

    def __str__(self):
        return '<分类>:<{}>'.format(self.name)

    class Meta:
        db_table = 'category'


class Articles(models.Model):
    author = models.CharField(max_length=10, default='zjh')
    title = models.CharField(max_length=20, unique=True, verbose_name='标题')
    content = MarkdownxField(verbose_name='内容')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='编辑时间')
    editor_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别',
                                 default=None)
    read_count = models.IntegerField(default=0, verbose_name='阅读人数')
    like_num_int = models.IntegerField(default=0, verbose_name='点赞人数')

    def __str__(self):
        return '<{}:{}>'.format(self.author, self.title)

    class Meta:
        db_table = 'article'


class Comment(models.Model):
    who = models.CharField(max_length=20, verbose_name='评论人')
    context = models.CharField(max_length=300, verbose_name='评论内容')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='评论文章')


class Person_tags(models.Model):
    tag = models.CharField(max_length=10, verbose_name='标签')
    articles = models.ManyToManyField(Articles)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return '<标签>:<{}>'.format(self.tag)
