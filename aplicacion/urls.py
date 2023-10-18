from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('producto', views.producto,name='producto'),
    path('producto/<codigo>', views.detalle,name='detalle'),
    path('index',views.IndexView.as_view(),name='index'),
    path('index/producto',views.ProductoView.as_view(),name='producto'),
    path('index/producto/<int:producto_id>',views.ProductoDetailView.as_view())

]
