from django.urls import path
#Подключение метода views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    #Создание дополнительной странички path - функция ('about' - страничка , views.about - обрашение к методу)
    #После этого создаем функцию about  в дериктори mysite/main/views
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

]