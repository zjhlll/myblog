from django.http import Http404
from django.shortcuts import render
from .models import Articles,Category,Person_tags
from django.core.paginator import Paginator
from utils.page import get_page_list
import markdown
# Create your views here.

def index(request):
    p_index =  int(request.GET.get('page',1))
    # 查询所有的文章显示5条
    article = Articles.objects.all()
    p = Paginator(article,1)
    total_page = p.num_pages
    if p_index > total_page:
        p_index = total_page
    article_list = p.page(p_index)
    # 构件页码信息
    page_list = get_page_list(total_page,p_index)
    # 查询所有的分类 分类名和每个分类下面的文章数
    cate_num_name = category_list()
    # 归档 年月 和文章数
    for article in article_list:
        article.content_notice = markdown.markdown(article.content).split()[0].split('>')[1]
    context = {
        'total_page':total_page,
        'title':'myblog',
        'article_list':article_list,
        'page_list':page_list,
        'p_index':p_index,
        'cate_num_name':cate_num_name,
        'year_month_num':month_list()
    }
    print(month_list())
    return render(request,'index.html',context=context)

def detail(requset,article_id):
    article = Articles.objects.filter(pk=article_id)
    if not article:
        return Http404()
    article = article[0]
    article_content = markdown.markdown(article.content)
    context = {
        'title':article.title,
        'article':article,
        'article_content':article_content,
        'year_month_num':month_list(),
        'cate_num_name':category_list(),
    }
    return render(requset,'singlepost.html',context)

def get_list(request,category,):
    # 查询对应的分类下的文章
    category = Category.objects.filter(name=category)
    if not category:
        return Http404
    category = category[0]

    p_index = int(request.GET.get('page',1))
    article_list = Articles.objects.filter(category=category)
    # 分页
    p = Paginator(article_list,1)
    total_page = p.num_pages
    if p_index > total_page:
        p_index = total_page
    article_list = p.page(p_index)
    # 返回的文章列表，需要缓存的内容为归档的内容
    for article in article_list:
        article.content_notice = markdown.markdown(article.content).split()[0].split('>')[1]
    context = {
        'title':category.name,
        'p_index':p_index,
        'total_page': total_page,
        'page_list':get_page_list(total_page,p_index),
        'article_list': article_list,
        'year_month_num':month_list(),
        'cate_num_name':category_list(),

    }
    return render(request,'list.html',context)


def month_list():
    articles = Articles.objects.all()
    year_month = set()
    for article in articles:
        year_month.add((article.editor_time.year,article.editor_time.month))
    counter = {}.fromkeys(year_month,0)
    for article in articles:
        counter[(article.editor_time.year,article.editor_time.month)] += 1
    year_month_number = []
    for key in counter:
        year_month_number.append([key[0],key[1],counter[key]])
    year_month_number.sort(reverse=True)
    return year_month_number

def category_list():
    category_list = Category.objects.all()
    cate_num_name = []
    for category in category_list:
        cate = {}
        cate['name'] = category.name
        cate['count'] = len(category.articles_set.all())
        cate_num_name.append(cate)
    return cate_num_name