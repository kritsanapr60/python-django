from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path(r'^signIn/', views.signIn, name='signIn'),
    path('postsign/', views.postsign, name='postsign'),
    path(r'^logout/', views.logout,name="log"),
    url(r'^signup/',views.signUp,name='signup'),
    url(r'^postsignup/',views.postsignup,name='postsignup'),
    path(r'^chap1$/', views.chap1, name='chap1'),
    path(r'^chap2$/', views.chap2, name='chap2'),
    path(r'^chap3$/', views.chap3, name='chap3'),
    path(r'^chap4$/', views.chap4, name='chap4'),   
    path(r'^chap5$/', views.chap5, name='chap5'),
    path(r'^chap6$/', views.chap6, name='chap6'),
    path(r'^chap7$/', views.chap7, name='chap7'),
    path(r'^chap8$/', views.chap8, name='chap8'),
    path(r'^chap9$/', views.chap9, name='chap9'),
    path(r'^chap10$/', views.chap10, name='chap10'),
    path(r'^chap11$/', views.chap11, name='chap11'),
    path(r'^chap12$/', views.chap12, name='chap12'),
    path(r'^chap13$/', views.chap13, name='chap13'),
    path(r'^chap14$/', views.chap14, name='chap14'),
    path(r'^chap15$/', views.chap15, name='chap15'),
    path(r'^chap16$/', views.chap16, name='chap16'),

]
