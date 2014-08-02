from django.shortcuts import render, RequestContext, render_to_response
from django.http import HttpResponse
from Tasks_List.models import Task
from Tasks_List.forms import Task_Form
from django.utils import timezone

# Create your views here.
def index(request):
    # Front Page
    # Shows current tasks
    tasks = Task.objects.all()
    tasks = [task for task in tasks if task.end_date > timezone.now()] # filter out expired tasks
    context = {'tasks': tasks}
    return render(request, 'Tasks_List/index.html', context)

def history(request):
    # See all tasks, even expired ones
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'Tasks_List/history.html', context)

def delete_task(request, name):
    # To Do: create delete link for each task in list
    # currently: .../delete/(task name)/ deletes task
    Task.objects.get(task_name=name).delete()
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'Tasks_List/index.html', context)

def add_task(request):
    # Add new tasks view
    context = RequestContext(request)
    if request.method == 'POST':
            form = Task_Form(request.POST)
            if form.is_valid():

                form.save(commit=True)

                return index(request)
            else:
                print form.errors
    else:
            form = Task_Form()
    return render_to_response('Tasks_List/addtask.html', {'form': form}, context)

# To Do: allow for a link to "cross items" out of the list