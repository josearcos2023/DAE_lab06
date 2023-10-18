from django.shortcuts import render
from .models import Producto,Categoria

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductoSerializer,CategoriaSerializer

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


class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class ProductoView(APIView):
    
    def get(self,request):
        dataProducto = Producto.objects.all()
        serProducto = ProductoSerializer(dataProducto,many=True)
        return Response(serProducto.data)
    
    def post(self,request):
        serProducto = ProductoSerializer(data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        
        return Response(serProducto.data)
    
class ProductoDetailView(APIView):
    
    def get(self,request,Producto_id):
        dataProducto = Producto.objects.get(pk=Producto_id)
        serProducto = ProductoSerializer(dataProducto)
        return Response(serProducto.data)
    
    def put(self,request,Producto_id):
        dataProducto = Producto.objects.get(pk=Producto_id)
        serProducto = ProductoSerializer(dataProducto,data=request.data)
        serProducto.is_valid(raise_exception=True)
        serProducto.save()
        return Response(serProducto.data)
    
    def delete(self,request,Producto_id):
        dataProducto = Producto.objects.get(pk=Producto_id)
        serProducto = ProductoSerializer(dataProducto)
        dataProducto.delete()
        return Response(serProducto.data)
