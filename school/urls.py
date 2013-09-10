from django.conf.urls import patterns  # , url

jornadas_urls = patterns('school',
    (r'^$', 'views.listarJornadas'),
    (r'^new', 'views.newJornada'),
    (r'^edit/(?P<id_jornada>.*)', 'views.editJornada'),
    (r'^delete/(?P<id_jornada>.*)', 'views.deleteJornada'),
)
PAcademico_urls = patterns('school',
    (r'^$', 'views.listarPAcademico'),
    (r'^new', 'views.newPAcademico'),
    (r'^edit/(?P<id_pAcademico>.*)', 'views.editPAcademico'),
    (r'^delete/(?P<id_pAcademico>.*)', 'views.deletePAcademico'),
)
