from django.urls import path
from . import views ,api

urlpatterns = [
    path('', views.index,name='index'),
    path('scan/',views.scan,name='scan'),
    path('view/',views.view_results,name='viewdata'),
    path('api/',api.finger_api,name='finger_api'),
    path('api/1',api.Finger_apii.as_view,name='Finger_apii'),
    path('api/<int:id>',api.Finger_creat.as_view,name='Finger_creat'),
    path('predict/', views.predict, name='predict'),
    path('<int:id>/',views.id_results,name='viewdata'),



]
