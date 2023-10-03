from django.shortcuts import render,get_object_or_404
from .models import Todo
from .forms import RegisterForm

def index(request):
    todo_list = Todo.objects.all().order_by('-id')
    context = {
        "todo_list": todo_list,
    }

    return render(request, 'todo/index.html', context)

def detail(request, id):
    todo = get_object_or_404(Todo, pk=id)
    context = {
        "todo": todo
    }

    return render(request, 'todo/detail.html', context)

def create(request):
    registerForm = RegisterForm()
    context = {
                'registerForm': registerForm,
                }
    return render(request, 'todo/create.html', context)

def register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()

    todo_list = Todo.objects.all().order_by('-id')
    context = {
                'todo_list': todo_list,
                }
    return render(request, 'todo/index.html', context)

def edit(request, id):
    todo = get_object_or_404(Todo, pk=id)
    registerForm = RegisterForm(instance=todo)    
    context = {
        "todo": todo,
        "registerForm": registerForm,
    }

    return render(request, 'todo/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=id)
        # instance=article：既存の記事の情報
        # request.POST：上書きする情報
        registerForm = RegisterForm(request.POST, instance=todo)
        print(registerForm.is_valid())
        if registerForm.is_valid():
            print("保存開始")
            todo.save()
            print('保存終了')
    todo_list = Todo.objects.all().order_by('-id')
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todo/index.html', context)

def delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    todo_list = Todo.objects.all().order_by('-id')

    context = {
        "todo_list": todo_list,
    }

    return render(request, 'todo/index.html', context)