from school import views
from django.urls import path


jornadas_urls = [
    # path('school'),
    path('/', views.listarJornadas),
    path('new/', views.newJornada),
    path('edit/<int:id_jornada>', views.editJornada),
    path('delete/<int:id_jornada>', views.deleteJornada),
]
PAcademico_urls = [
    # path('school'),
    path('', views.listarPAcademico),
    path('new', views.newPAcademico),
    path('edit/<int:id_pAcademico>', views.editPAcademico),
    path('delete/<int:id_pAcademico>', views.deletePAcademico),
]
