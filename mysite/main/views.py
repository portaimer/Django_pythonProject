#render метод отбражения html шаблон
from django.shortcuts import render
#Подключение метода отображения текста HttpResponse
from django.http import HttpResponse
# Create your views here.

#Функция для отображения Главной странички
#Для отображения html шаблона возвращаем #return функци #render (передвть пораметры request и 'путь к шаблону / название шаблона')
def index(request):
    return render(request, 'main/index.html')

# Функия для отбражения странички about
def about(request):
    return render(request, 'main/about.html')