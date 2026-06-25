from django.db import models

# Create your models here.

class Origin(models.Model):
    origin_id = models.AutoField(primary_key=True)
    origin_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'origin'

    def __str__(self):
        return self.origin_name
