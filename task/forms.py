from django.forms import ModelForm
from .models import Tasks


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ('task_title', 'task_description', 'task_pic')

    def clean(self):
        task_title = self.cleaned_data.get('task_title')
        if len(task_title) < 10:
            self._errors['task_title'] = self.error_class(
                ['Minimum length should be 10.'])