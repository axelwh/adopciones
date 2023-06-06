from django.conf.urls import url
from apps_adopciones.adopcion.views import solicitudes_create, solicitudes_read_all, solicitudes_update, \
    solicitudes_delete, SolicitudReadAll, SolicitudCreate, SolicitudUpdate, SolicitudDelete, solicitudes_index

urlpatterns = [
    url(r'^$', solicitudes_index, name='solicitudes_index'),
    url(r'^funciones/crear$', solicitudes_create, name='solicitudes_funciones_crear'),
    url(r'^funciones$', solicitudes_read_all, name='solicitudes_funciones'),
    url(r'^funciones/editar/(?P<id_solicitud>\d+)$', solicitudes_update, name='solicitudes_funciones_editar'),
    url(r'^funciones/eliminar/(?P<id_solicitud>\d+)$', solicitudes_delete, name='solicitudes_funciones_eliminar'),
    url(r'^clases/crear$', SolicitudCreate.as_view(), name='solicitudes_clases_crear'),
    url(r'^clases$', SolicitudReadAll.as_view(), name='solicitudes_clases'),
    url(r'^clases/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='solicitudes_clases_editar'),
    url(r'^clases/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='solicitudes_clases_eliminar')
]
