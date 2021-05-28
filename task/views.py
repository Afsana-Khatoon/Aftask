from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TasksForm
from django.contrib import messages
from .models import Tasks
from django.core.paginator import Paginator


@login_required
def index(request):
    form = TasksForm()
    tasks = Tasks.objects.all().filter(uid=request.user).order_by('-create_time_stamp')
    paginator = Paginator(tasks, 5)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)     
    if request.POST:
        form = TasksForm(request.POST, request.FILES)
        form.instance.uid = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully')
            return redirect('index')
       
    context = {
        'form': form,
        'tasks': tasks
    }
    return render(request, 'task/index.html', context=context)
