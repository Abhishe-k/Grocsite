from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_object_or_404, render
from .forms import InterestForm, OrderItemForm, OrderItem

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

def itemdetail(request, item_id):
    try:
        item_by_id = Item.objects.get(id=item_id)
        if request.POST:
            form = InterestForm(request.POST)
            if form.is_valid():
                print("In interest form")
                interested = form.cleaned_data["interested"]
                print(interested)
                quantity = form.cleaned_data["quantity"]
                print(quantity)
                comments = form.cleaned_data["comments"]
                print(comments)
                i = item_by_id.interested + int(interested)
                item_by_id.interested = i
                print(item_by_id)
                item_by_id.save()
        form = InterestForm()
        return render(request, 'myapp1/itemdetail.html', {'item': item_by_id, 'form': form})
    except:
        context = {'msg': "Item with Item id " + str(item_id) + " does not exist!"}
        return render(request, 'myapp1/itemdetail.html', context)




def placeorder(request):
    msg = ''
    itemlist = Item.objects.all()
    orderitem = OrderItem.objects.all()[0]
    print(orderitem)
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            print(str(order))
            if order.qty_ordered <= order.item.stock:
                print(str(order))
                item = Item.objects.get(id=order.item.id)
                updated_stock = item.stock - order.qty_ordered
                item.stock = updated_stock
                item.save(force_update=True)
                order.save()
                msg = 'Your order has been placed successfully.'
            else:
                msg = 'We do not have sufficient stock to fill your order.'
                print(msg)
                return render(request, 'myapp1/order_response.html', {'msg': msg})
    else:
        form = OrderItemForm()
    return render(request, 'myapp1/placeorder.html', {'form': form, 'msg': msg, 'itemlist': itemlist})

