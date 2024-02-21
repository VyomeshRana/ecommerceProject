from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cusReg/', views.customerReg, name='cusReg'),
    path('venReg/',  views.venderReg, name='venReg'),

]
