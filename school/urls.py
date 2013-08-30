from django.conf.urls import patterns  # , url

jornadas_urls = patterns('school',
    (r'^$', 'views.listarJornadas'),
    (r'^new', 'views.newJornada'),
    (r'^edit/(?P<id_jornada>.*)', 'views.editJornada'),
    (r'^delete/(?P<id_jornada>.*)', 'views.deleteJornada'),
)
