import csv
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
# Create your views here.

#clase para mostrar lista de productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'lista_productos.html'
    context_object_name = 'productos'
#clase para crear el producto
class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre','precio','stock','categoria']
    template_name = 'producto_formulario.html'
    success_url = reverse_lazy('producto-list')

#clase para editar el producto
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'stock', 'categoria']
    template_name = 'producto_formulario.html'
    success_url = reverse_lazy('producto-list')

#clase para borrar el producto
class ProductoDeleteView(DeleteView):
    model = Producto
    fields = '__all__'
    template_name = 'conf_borrar.html'
    success_url = reverse_lazy('producto-list')

#Exportar csv
def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="productos.csv"'
    writer = csv.writer(response)

    writer.writerow(['Id', 'nombre', 'precio', 'stock'])
    productos = Producto.objects.all()
    for producto in productos:
        writer.writerow([producto.id, producto.nombre, producto.precio,producto.stock])
    return response



    

