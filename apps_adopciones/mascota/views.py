from django.shortcuts import render, redirect
from apps_adopciones.mascota.forms import MascotaForm
from apps_adopciones.mascota.models import Mascota
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


def mascotas_index(request):
    return render(request, 'mascota/mascota_index.html')


# Create your views here.
def mascotas_create(request):
    form = MascotaForm(request.GET)
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mascotas:mascotas_funciones')
    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascotas_read_all(request):
    mascotas = Mascota.objects.all().order_by('id')
    contexto = {
        'mascotas': mascotas,
        'url_names': {
            'update': 'mascotas:mascotas_funciones_editar',
            'delete': 'mascotas:mascotas_funciones_eliminar'
        }
    }
    return render(request, 'mascota/mascota_list.html', contexto)


def mascotas_update(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    form = MascotaForm(instance=mascota)
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascotas:mascotas_funciones')
    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascotas_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascotas:mascotas_funciones')
    context = {
        'mascota': mascota,
        'url_names': {
            'show_all': 'mascotas:mascotas_funciones'
        }
    }
    return render(request, 'mascota/mascota_delete.html', context)


class MascotasReadAll(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'

    def get_context_data(self, **kwargs):
        context = super(MascotasReadAll, self).get_context_data(**kwargs)
        mascotas = self.model.objects.all()
        context['mascotas'] = mascotas
        context['url_names'] = {
            'update': 'mascotas:mascotas_clases_editar',
            'delete': 'mascotas:mascotas_clases_eliminar'
        }
        return context


class MascotasCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascotas:mascotas_clases')


class MascotasUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascotas:mascotas_clases')


class MascotasDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascotas:mascotas_clases')

    def get_context_data(self, **kwargs):
        context = super(MascotasDelete, self).get_context_data(**kwargs)
        id_mascota = self.kwargs.get('pk', 0)
        mascota = self.model.objects.get(id=id_mascota)
        context['mascota'] = mascota
        context['url_names'] = {
            'show_all': 'mascotas:mascotas_clases'
        }
        return context
