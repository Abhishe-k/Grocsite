from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_object_or_404, render


# Create your views here.
# def index(request):
#     type_list = Item.objects.all().order_by('-price')[:7]
#     response = HttpResponse()
#     heading1 = '<p>' + 'Different Types: ' + '</p>'
#     response.write(heading1)
#     for type in type_list:
#         para = '<p>' + str(type.id) + ': ' + str(type) + '</p>'
#         response.write(para)
#     return response

def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})


def about(request):
    # return HttpResponse("This is an Online Grocery Store")
    return render(request, 'myapp1/about0.html')


def detail(request, type_no):
    type_by_id = get_object_or_404(Type, id=type_no)
    item_by_type = Item.objects.filter(type_id=type_no)
    # response = HttpResponse()
    para = '<p>' + str(type_by_id.id) + ': ' + str(type_by_id.name) + '</p>'
    # response.write(para)
    # return response
    return render(request, 'myapp1/detail0.html', {'type': type_by_id, 'items': item_by_type})


def items(request):
    itemlist = Item.objects.all().order_by('id')[:20]
    return render(request, 'myapp1/items.html', {'itemlist': itemlist})


def placeorder(request):
    return HttpResponse("You can place your order here.")