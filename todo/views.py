from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm, NewTodoForm

def index(request):
    todo_list = Todo.objects.order_by('id')

    # form = TodoForm()
    newtodoform = NewTodoForm()

    context = {'todo_list' : todo_list, 'form' : newtodoform}

    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    # form = TodoForm(request.POST)


    
    # todo_6 = Todo.objects.get(pk=6)
    # newtodoform = NewTodoForm(request.POST, instance=todo_6)
    newtodoform = NewTodoForm(request.POST)

    if newtodoform.is_valid():
        # new_todo = Todo(text=newtodoform.cleaned_data['text'])
        # new_todo.save()

        new_todo = newtodoform.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def incompleteTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = False
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')

