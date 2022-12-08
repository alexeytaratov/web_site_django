from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task # Название модели, с которой работаем
        fields = ['title', 'task'] # столбцов модели
        widgets = { # внизу короче одёт описание полей для ввода
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название"
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"
            })
        }