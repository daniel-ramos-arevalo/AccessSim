from django.db import models


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'status'
        
    def __str__(self):
        return self.status_name
    