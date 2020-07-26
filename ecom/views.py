from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import cartData

# Create your views here.
def jersey(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

   
    products = Product.objects.filter(category="Jersey")
    context = {'products':products,'order':order,'cartItems':cartItems}
    return render(request,"jersey.html",context)

def kit(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

   
    products = Product.objects.filter(category="Kit")
    context = {'products':products,'items':items,'order':order,'cartItems':cartItems}
    return render(request,"kit.html",context)

def others(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

   
    products = Product.objects.filter(category="Others")
    context = {'products':products,'items':items,'order':order,'cartItems':cartItems}
    return render(request,"others.html",context)

def detail(request,pk):
    product = Product.objects.get(id=pk)
    print(product)
    context = {'product':product}
    return render(request,"detail.html",context)

def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request,"cart.html",context)

def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items,'order':order,'cartItems':cartItems}
    return render(request,"checkout.html",context)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def updateOrder(request):
    data=json.loads(request.body)
    productId  = data['productId']
    action = data['action']
    print('Action:',action)
    print('ProductId:',productId)

    customer = request.user.customer
    print(customer)
    product = Product.objects.get(id=productId)
    print(product)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    print(order)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action=='add':
        orderItem.quantity = (orderItem.quantity) + 1
    elif action=='remove':
        orderItem.quantity = (orderItem.quantity) - 1
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse("You can update order here.",safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    total = float(data['shipping']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['province'],
        zipcode=data['shipping']['zipcode'],

    )

    print('address : ',data['shipping']['city'])
    return JsonResponse("processing order",safe=False)