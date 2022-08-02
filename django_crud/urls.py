
from django.conf.urls import include, url
from django.urls import include, path
from school.urls import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from website import views
admin.autodiscover()

urlpatterns = [
    # Examples:
    path('', views.home, name="home"),
    # url(r'^django_crud/', include('django_crud.foo.urls')),
    path('jornadas/', include(jornadas_urls)),
    path('programas/', include(PAcademico_urls)),
    # # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
]
