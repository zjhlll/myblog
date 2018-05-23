from django.shortcuts import render
from .models import Articles,Category,Person_tags
from django.core.paginator import Paginator
from utils.page import get_page_list
# Create your views here.

def index(request):
    p_index = 1
    # 查询所有的文章显示5条
    article = Articles.objects.all()
    p = Paginator(article,5)
    total_page = p.num_pages
    article_list = p.page(p_index)
    # 构件页码信息
    page_list = get_page_list(total_page,p_index)
    # 查询所有的分类 分类名和每个分类下面的文章数
    category_list = Category.objects.all()
    cate_num_name = []
    for category in category_list:
        cate = {}
        cate['name'] = category.name
        cate['count'] = len(category.articles_set.all())
        cate_num_name.append(cate)
    # 归档 年月 和文章数
    context = {
        'title':'myblog',
        'article_list':article_list,
        'page_list':page_list,
        'p_index':p_index,
        'category':category_list,
        'cate_num_name':cate_num_name,
        'year_month_num':month_list()
    }
    print(month_list())
    return render(request,'index.html',context=context)

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