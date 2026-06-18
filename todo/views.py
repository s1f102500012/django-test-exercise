from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware

from todo.models import Task


def index(request):
    if request.method == 'POST':
        due_at = None
        if request.POST.get('due_at'):
            due_at = make_aware(parse_datetime(request.POST['due_at']))
        task = Task(title=request.POST['title'], due_at=due_at)
        task.save()
    if request.GET.get('order') == 'due':
        tasks = Task.objects.order_by('due_at')
    else:
        tasks = Task.objects.order_by('-posted_at')
    context = {
        'tasks': tasks,
    }
    return render(request, 'todo/index.html', context)
