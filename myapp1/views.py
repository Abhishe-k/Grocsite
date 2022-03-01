from django.shortcuts import render
from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    type_list = Item.objects.all().order_by('-price')[:7]
    response = HttpResponse()
    heading1 = '<p>' + 'Different Types: ' + '</p>'
    response.write(heading1)
    for type in type_list:
        para = '<p>' + str(type.id) + ': ' + str(type) + '</p>'
        response.write(para)
    return response


def about(request):
    return HttpResponse("This is an Online Grocery Store")

def detail(request, type_no):
    type_by_id = get_object_or_404(Type, id=type_no)
    response = HttpResponse()
    para = '<p>' + str(type_by_id.id) + ': ' + str(type_by_id.name) + '</p>'
    response.write(para)
    return response
