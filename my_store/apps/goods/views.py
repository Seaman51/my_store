from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Good
from .forms import GoodForm

def index(request):
    goods_list = Good.objects.all()
    return render(request, 'goods/good_list.html', {'title': 'Главная страница сайта', 'goods_list': goods_list})


def create(request):
    if request.method == 'POST':
        form = GoodForm(request.POST)
        data = save_good_form(request, form, 'goods/good_create.html')
    else:
        data = {
            'form_is_valid': False,
            'html_form': render_to_string('goods/good_create.html', {'form': GoodForm()}, request=request)
        }

    return JsonResponse(data)

def save_good_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            goods = Good.objects.all()
            data['html_good_list'] = render_to_string('goods/partial_goods_list.html', {
                'goods_list': goods
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return data