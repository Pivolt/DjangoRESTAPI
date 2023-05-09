from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    status = models.CharField(choices=(
        ('Nowy', 'Nowy'),
        ('W toku', 'W toku'),
        ('Rozwiązany', 'Rozwiązany')
    ), default='Nowy')
    assigned_user = models.ForeignKey(User, 
                                              null=True,
                                              blank=True,
                                              on_delete=models.SET_NULL)
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        super(Task, self).save(force_insert, force_update, *args, **kwargs)
        TaskHistory.objects.create(task=self, 
                                   name=self.name, 
                                   description=self.description,
                                   status=self.status,
                                   assigned_user=self.assigned_user)

class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(choices=(
        ('Nowy', 'Nowy'),
        ('W toku', 'W toku'),
        ('Rozwiązany', 'Rozwiązany')
    ), default='Nowy')
    assigned_user = models.ForeignKey(User, 
                                              null=True,
                                              blank=True,
                                              on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)