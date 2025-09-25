from django.urls import path

from . import views

app_name = "boardApp"

urlpatterns = [
    path('', views.index, name='index'), # boardApp/
    path('<int:question_id>/', views.detail, name='detail'), # boardApp/3/
    # /boardApp/answer/create/3/
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]