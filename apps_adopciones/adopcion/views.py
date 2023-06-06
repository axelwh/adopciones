from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps_adopciones.adopcion.models import Solicitud, Persona
from apps_adopciones.adopcion.forms import SolicitudForm, PersonaForm
from django.core.urlresolvers import reverse_lazy


def solicitudes_index(request):
    return render(request, 'adopcion/solicitud_index.html')


def solicitudes_create(request):
    persona_form = PersonaForm(request.GET)
    solicitud_form = SolicitudForm(request.GET)
    if request.method == 'POST':
        persona_form = PersonaForm(request.POST)
        solicitud_form = SolicitudForm(request.POST)
        if persona_form.is_valid() and solicitud_form.is_valid():
            solicitud = solicitud_form.save(commit=False)
            solicitud.persona = persona_form.save()
            solicitud.save()
            return HttpResponseRedirect(reverse_lazy('solicitudes:solicitudes_funciones'))
    context = {
        'persona_form': persona_form,
        'solicitud_form': solicitud_form
    }
    return render(request, 'adopcion/solicitud_form.html', context)


def solicitudes_read_all(request):
    solicitudes = Solicitud.objects.all()
    context = {
        'solicitudes': solicitudes,
        'url_names': {
            'update': 'solicitudes:solicitudes_funciones_editar',
            'delete': 'solicitudes:solicitudes_funciones_eliminar'
        }
    }
    return render(request, 'adopcion/solicitud_list.html', context)


def solicitudes_update(request, id_solicitud):
    solicitud = Solicitud.objects.get(id=id_solicitud)
    persona = Persona.objects.get(id=solicitud.persona_id)
    solicitud_form = SolicitudForm(instance=solicitud)
    persona_form = PersonaForm(instance=persona)
    if request.method == 'POST':
        solicitud_form = SolicitudForm(request.POST, instance=solicitud)
        persona_form = PersonaForm(request.POST, instance=persona)
        if solicitud_form.is_valid() and persona_form.is_valid():
            solicitud_form.save()
            persona_form.save()
            return HttpResponseRedirect(reverse_lazy('solicitudes:solicitudes_funciones'))
    context = {
        'persona_form': persona_form,
        'solicitud_form': solicitud_form
    }
    return render(request, 'adopcion/solicitud_form.html', context)


def solicitudes_delete(request, id_solicitud):
    solicitud = Solicitud.objects.get(id=id_solicitud)
    persona = Persona.objects.get(id=solicitud.persona_id)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('solicitudes:solicitudes_funciones')
    context = {
        'persona': persona,
        'url_names': {
            'show_all': 'solicitudes:solicitudes_funciones'
        }
    }
    return render(request, 'adopcion/solicitud_delete.html', context)


class SolicitudReadAll(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'

    def get_context_data(self, **kwargs):
        context = super(SolicitudReadAll, self).get_context_data(**kwargs)
        solicitudes = self.model.objects.all()
        context['solicitudes'] = solicitudes
        context['url_names'] = {
            'update': 'solicitudes:solicitudes_clases_editar',
            'delete': 'solicitudes:solicitudes_clases_eliminar'
        }
        return context


class SolicitudCreate(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    persona_form_class = PersonaForm
    template_name = 'adopcion/solicitud_form.html'
    success_url = reverse_lazy('solicitudes:solicitudes_clases')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'solicitud_form' not in context:
            context['solicitud_form'] = self.form_class(self.request.GET)
        if 'persona_form' not in context:
            context['persona_form'] = self.persona_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        solicitud_form = self.form_class(request.POST)
        persona_form = self.persona_form_class(request.POST)
        if solicitud_form.is_valid() and persona_form.is_valid():
            solicitud = solicitud_form.save(commit=False)
            solicitud.persona = persona_form.save()
            solicitud.save()
            self.object = solicitud
            return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(
            persona_form=persona_form,
            solicitud_form=solicitud_form
        ))


class SolicitudUpdate(UpdateView):
    model = Solicitud
    form_class = SolicitudForm
    persona_model = Persona
    persona_form_class = PersonaForm
    template_name = 'adopcion/solicitud_form.html'
    success_url = reverse_lazy('solicitudes:solicitudes_clases')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.persona_model.objects.get(id=solicitud.persona_id)
        if 'solicitud_form' not in context:
            context['solicitud_form'] = self.form_class(instance=solicitud)
        if 'persona_form' not in context:
            context['persona_form'] = self.persona_form_class(instance=persona)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwars):
        self.object = None
        id_solicitud = kwars['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.persona_model.objects.get(id=solicitud.persona_id)
        solicitud_form = self.form_class(request.POST, instance=solicitud)
        persona_form = self.persona_form_class(request.POST, instance=persona)
        if solicitud_form.is_valid() and persona_form.is_valid():
            solicitud_form.save()
            persona_form.save()
            self.object = solicitud_form
            return HttpResponseRedirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(
            persona_form=persona_form,
            solicitud_form=solicitud_form
        ))


class SolicitudDelete(DeleteView):
    model = Solicitud
    persona_model = Persona
    template_name = 'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('solicitudes:solicitudes_clases')

    def get_context_data(self, **kwargs):
        context = super(SolicitudDelete, self).get_context_data(**kwargs)
        id_solicitud = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.persona_model.objects.get(id=solicitud.persona_id)
        context['persona'] = persona
        context['url_names'] = {
            'show_all': 'solicitudes:solicitudes_clases',
        }
        return context
