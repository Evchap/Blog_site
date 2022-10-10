from django import template
from musicians.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all() # возвращвет список
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('musicians/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all() # возвращает фрагмент страницы
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}

