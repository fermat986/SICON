from django.shortcuts import render
from .forms import RepuestoForm
from django.http import HttpResponseRedirect,HttpResponse
from .models import Repuesto,Marca,Empleado,Gerente,JefeTaller
from django import forms
from SICON.reparacion.views_inventario import registro_inventario
from django.contrib.auth.decorators import user_passes_test
import json
# Create your views here.
@user_passes_test(lambda u: u.has_perm('administrador.add_repuesto'),login_url="/indexAdmin")
def crear_repuesto(request):
    repuesto = RepuestoForm()
    exito = False
    post = False
    if request.method=='POST':
        repuesto = RepuestoForm(request.POST)
        id = request.session["id"]
        empleado = Gerente.objects.filter (user_ptr_id = id).first()
        if empleado is None :
            empleado = JefeTaller.objects.filter (user_ptr_id = id).first()
        r = Repuesto.objects.filter (codigo =request.POST['codigo'], sucursal = empleado.sucursal).first()
        if not r is None:
            post = True
    if (repuesto.is_valid() and r is  None):
        repuest =  repuesto.save(commit=False)
        repuest.sucursal = empleado.sucursal
        repuest.save()
        exito = True
        repuesto = RepuestoForm()
        return HttpResponseRedirect('/repuestos/')
    return render(request, 'crear_repuesto.html', {'form':repuesto,'exito':exito,'post' : post} )




@user_passes_test(lambda u: u.has_perm('administrador.listar_Repuestos'),login_url="/indexAdmin")
def listar_repuestos(request):
    id = request.session["id"]
    print id
    empleado = Gerente.objects.filter (user_ptr_id = id).first()
    if empleado is None :
        empleado = JefeTaller.objects.filter (user_ptr_id = id).first()
    repuestos = Repuesto.objects.filter(sucursal = empleado.sucursal)
    return render(request,'lista_repuestos.html',{'repuestos':repuestos})


@user_passes_test(lambda u: u.has_perm('administrador.change_repuesto'),login_url="/indexAdmin")
def editar_repuesto(request, id):
    id_session = request.session["id"]
    empleado = Gerente.objects.filter (user_ptr_id = id_session).first()
    if empleado is None :
        empleado = JefeTaller.objects.filter (user_ptr_id = id_session).first()
    repuestos = Repuesto.objects.filter(sucursal = empleado.sucursal)
    repuesto = Repuesto.objects.get(pk = id)
    form_edicion = RepuestoForm(instance=repuesto, initial=repuesto.__dict__)
    if request.method == 'POST':
        form_edicion = RepuestoForm(request.POST, instance=repuesto, initial=repuesto.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                form_edicion.save()
                return HttpResponseRedirect("/repuestos")
        else:
            return HttpResponseRedirect("/repuestos")
    return render(request, 'lista_repuestos.html', {'repuestos': repuestos,'repuesto':repuesto, 'edicion': True, 'form_edicion': form_edicion})

@user_passes_test(lambda u: u.has_perm('reparacion.add_inventario'),login_url="/indexAdmin")
def inventario (request,id):
    print ("inventario")
    repuestos= Repuesto.objects.all()
    repuesto = Repuesto.objects.get(pk = id)
    if request.method == 'POST':
        cantidad = request.POST['cantidad_inv']
        registro_inventario(repuesto,'entrada',cantidad);
        return HttpResponseRedirect('/repuestos/')
    return render(request, 'lista_repuestos.html', {'repuestos': repuestos, 'inventario': True, 'rep': repuesto})


# def cargar_modelos (request):
#         opcion =request.GET['option']
#         modelos = Modelo.objects.filter(marca = opcion)
#         string_respuesta = ""
#         for modelo in modelos:
#             string_respuesta += str(modelo.id)+":"+modelo.nombre+","
#         string_respuesta = string_respuesta[0:-1]
#
#         return HttpResponse(string_respuesta)

@user_passes_test(lambda u: u.has_perm('administrador.delete_repuesto'),login_url="/indexAdmin")
def eliminar_repuesto(request, id):
    repuesto= Repuesto.objects.get(id=id)
    if repuesto.activo:
        repuesto.activo = False
    else:
        repuesto.activo = True
    repuesto.save()
    return HttpResponseRedirect("/repuestos")
