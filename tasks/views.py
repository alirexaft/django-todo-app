from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import AddTaskForm, Task_information_form
from .models import Task


class TaskList(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = AddTaskForm()
        tasks = Task.objects.filter(user=self.request.user)
        return render(request, 'tasks.html', {'form': form, 'user': self.request.user, 'tasks': tasks})

    def post(self, request):
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = Task()
            task.title = form.cleaned_data['title']
            task.user = self.request.user
            task.save()

            tasks = Task.objects.filter(user=self.request.user)
            return render(request, 'tasks.html', {'tasks': tasks, 'user': self.request.user})


@login_required(login_url='/accounts/login/')
def updatetask(request, pk):
    task = Task.objects.get(id=pk)
    form = Task_information_form(instance=task)
    if request.method == 'POST':
        form = Task_information_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    constext = {'form': form, 'task': task}
    return render(request, 'task-information.html', constext)


@login_required(login_url='/accounts/login/')
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('tasks')
