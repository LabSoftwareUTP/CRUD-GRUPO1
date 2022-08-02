from school import views
from django.urls import path

jornadas_urls = [
    # path('school'),
    path('', views.listarJornadas, name="list-journey"),
    path('new/', views.newJornada, name="create-journey"),
    path('edit/<int:id_jornada>', views.editJornada, name="edit-journey"),
    path('delete/<int:id_jornada>', views.deleteJornada, name="delete-journey"),
]
PAcademico_urls = [
    # path('school'),
    path('', views.listarPAcademico),
    path('new', views.newPAcademico),
    path('edit/<int:id_pAcademico>', views.editPAcademico),
    path('delete/<int:id_pAcademico>', views.deletePAcademico),
]
