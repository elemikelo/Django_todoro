from django.db import models

class Task(models.Model):

    PENDING = "PEN"
    DONE = "DON"
    STATUSES = (
        (PENDING, "Pending"),
        (DONE, "Done")
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=3, default=PENDING, choices=STATUSES) # Pendiente, hecha
    time_estimated = models.IntegerField(null=True)
    deadline = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True) # automaticamente añada la fecha de creación
    modified_at = models.DateTimeField(auto_now=True) # automaticamente actualiza la fecha al guardar

