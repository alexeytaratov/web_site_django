from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all() # тут мы всю таблицу из БД запиховаем в переменную

    # tasks = Task.objects.order_by('id')
    # order_by - сортировка, в скобках пишется имя столбца,
    # по которому будем сортировать (в примере будем сортировать по столбцу АЙДИ.
    # Если в скобках написать, например, ('-id'), то элементы будут выводиться в обратном порядке.
    # Если после ('id') написать [:5], то выведутся 5 элементов данной таблицы.

    return render(request, 'mainApp/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})
    # метод render - указываем, какой HTML-шаблон будет подключен.
    # request - аргумент, который ставится по дефолту.
    # mainApp/index.html - указываем путь к файлу HTML.
    # 3 аргумент - это для заполения HTML-шаблона
def about(request):
    return render(request, 'mainApp/about.html')

def create(request):
    error = ''
    if request.method == 'POST': # Этот код означает: Если данные передаются с помощью метода ПОСТ,
                                 # то значит мы их получаем и они корректные и мы их сохраняем, как новую запись в БД.
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # после добавления записи переадресует на главную страничку
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainApp/create.html', context)