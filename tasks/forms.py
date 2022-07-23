from django import forms
from .models import Task


class AddTaskForm(forms.Form):
    title = forms.CharField()


class Task_information_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_complete']
