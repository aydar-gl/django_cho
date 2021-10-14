from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Category, Order, Dish, Station
from django.views.generic.base import View
from .forms import Adding, BuyForm
from django.conf import settings
from django.core.mail import send_mail

def index_view(request):
    return render(request, 'WebFront/index.html')

def category_view(request):
    categories = Category.objects.all()
    return render(request, 'WebFront/category.html', {'categories': categories})

class Menu_view(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        dishes = Dish.objects.filter(category=category.id)
        return render(request, 'WebFront/menu.html', {'dishes': dishes})

list = []

def adding(request, category_slug, dish_slug):
    dish = Dish.objects.get(slug=dish_slug)
    if request.method == 'POST':
        add_form = Adding(request.POST)
        if add_form.is_valid():
            list.append(dish)
            return HttpResponseRedirect('/category/')
    else:
        add_form = Adding()
    return render(request, 'WebFront/dish.html', {'dish': dish, 'add_form':add_form})

def basket_view(request):
    order_price = 0
    for dish in list:
        order_price += dish.price
    if request.method == 'POST':
        buy_form = BuyForm(request.POST)
        if buy_form.is_valid() and list:
            new_order = Order(client_name=buy_form.cleaned_data['client_name'], client_number=buy_form.cleaned_data['client_number'], client_mail=buy_form.cleaned_data['client_mail'],
                              order_price=order_price, station=buy_form.cleaned_data['station'])
            new_order.save()
            dish_msg = ''
            for e in list:
                new_order.dishes.add(e)
                dish_msg += f'{e.name}, '
            msg = f'Уважаемый, {new_order.client_name} ({new_order.client_number}), Вы сделали заказ в ресторане Cho на сумму {new_order.order_price} руб. Состав заказа: {dish_msg[:-2]}.'
            send_mail('Заказ в ресторане Cho', msg, settings.EMAIL_HOST_USER, [new_order.client_mail])
            return HttpResponseRedirect('/')
    else:
        buy_form = BuyForm()
    return render(request, 'WebFront/basket.html', {'list': list, 'buy_form': buy_form, 'order_price': order_price})

def clear_basket(request):
    list.clear()
    return HttpResponseRedirect('/basket/')