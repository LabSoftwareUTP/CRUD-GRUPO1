from django.urls import path


jornadas_urls = [
    path('school'),
    path('$', 'views.listarJornadas'),
    path('new', 'views.newJornada'),
    path('edit/(?P<id_jornada>.*)', 'views.editJornada'),
    path('delete/(?P<id_jornada>.*)', 'views.deleteJornada'),
]
PAcademico_urls = [
    path('school'),
    path('', 'views.listarPAcademico'),
    path('new', 'views.newPAcademico'),
    path('edit/(?P<id_pAcademico>.*)', 'views.editPAcademico'),
    path('delete/(?P<id_pAcademico>.*)', 'views.deletePAcademico'),
]
