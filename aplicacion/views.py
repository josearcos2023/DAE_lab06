from django.shortcuts import render
from .models import Producto,Categoria
# Create your views here.
def index(request):
    product_list=Producto.objects.order_by('nombre')
    category_list=Categoria.objects.order_by('nombre')
    context={
        'product_list':product_list,
        'category_list':category_list
    }
    return render(request,'index.html', context)

def producto(request):
    return render(request,'producto.html')

def detalle(request,codigo):
    producto=Producto.objects.get(id=codigo)
    context={
        'producto':producto
    }
    return render(request,"detalles.html",context)

