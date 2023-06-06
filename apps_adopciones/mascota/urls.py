from django.conf.urls import url

from views import mascotas_create, mascotas_read_all, mascotas_update, mascotas_delete, \
    MascotasReadAll, MascotasCreate, MascotasUpdate, MascotasDelete, mascotas_index

urlpatterns = [
    url(r'^$', mascotas_index, name='mascotas_index'),
    url(r'^funciones/crear$', mascotas_create, name='mascotas_funciones_crear'),
    url(r'^funciones$', mascotas_read_all, name='mascotas_funciones'),
    url(r'^funciones/editar/(?P<id_mascota>\d+)$', mascotas_update, name='mascotas_funciones_editar'),
    url(r'^funciones/eliminar/(?P<id_mascota>\d+)$', mascotas_delete, name='mascotas_funciones_eliminar'),
    url(r'^clases/crear$', MascotasCreate.as_view(), name='mascotas_clases_crear'),
    url(r'^clases$', MascotasReadAll.as_view(), name='mascotas_clases'),
    url(r'^clases/editar/(?P<pk>\d+)$', MascotasUpdate.as_view(), name='mascotas_clases_editar'),
    url(r'^clases/eliminar/(?P<pk>\d+)$', MascotasDelete.as_view(), name='mascotas_clases_eliminar'),
]
