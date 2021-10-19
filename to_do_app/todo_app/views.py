from django.shortcuts import render
from todo_app.models import Todo

def index(request):
    context={
        'todos': Todo.objects.all()
    }
    return render(request, "todos_app/index.html",context)

