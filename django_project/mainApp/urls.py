# КОПИРУЕМ СЮДА КОД ИЗ ФАЙЛА URLS.PY ИЗ ПАПКИ DJANGO_PROJECT
from django.urls import path
from . import views # пишем о том, что из этой же директории, в которой находимся, мы импортируем файл views.py

urlpatterns = [
    path('', views.index, name='home'), # сюда идёт переход из файла django_project\urls.py
                          # Если пользователь переходит на главную страничку,
                          # то в таком случае обращаемся к файлу views.py и методу index.
                          # name="home" - так лучше записывать ссылки (они будут указываться в html-файлах)
    path('about-us', views.about, name='about'), # если пользователь к url-адресу добавит "about-us",
                                  # то он попадёт на страничку"о нас", которую мы создадим.
                                  # То есть, программа из файла mainApp\urls.py перейдёт
                                  # в файл views.py и выполнить метод about оттуда
    path('create', views.create, name='create'),
]
