from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Tasks(models.Model):
    tid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200)
    task_description = models.TextField(max_length=2000, blank=True, null=True)
    task_pic = models.ImageField(upload_to='task_image', blank=True)
    create_time_stamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'Task: {self.tid} create_time_stamp: {self.create_time_stamp}'

    class Meta:
        verbose_name_plural = 'Tasks'
