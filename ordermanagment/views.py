from django.http import HttpResponse
from django.shortcuts import render
from .models import orders
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the order management home page.")

# Finding all orders
def all_orders(request):
    all_orders = orders.objects.all().order_by('-order_name')
    paginator = Paginator(all_orders, 10)  # Show 10 orders per page
    page_number = request.GET.get('page')
    try:
        all_orders = paginator.page(page_number)
    except PageNotAnInteger:
        all_orders = paginator.page(1)
    except EmptyPage:
        all_orders = paginator.page(paginator.num_pages)
    return render(request, 'all_orders.html', {'all_orders': all_orders})