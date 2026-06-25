from django.db import models
from status.models import Status
from origin.models import Origin

# Create your models here.

class Leads(models.Model):
    lead_id = models.AutoField(primary_key=True)
    lead_name = models.CharField(max_length=150, null=False, db_index=True)
    email = models.CharField(max_length=150, unique=True, null=False)
    lead_message = models.CharField(max_length=500, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    
    # Foreign Keys corretas
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        db_column='status_id',
        to_field='status_id'
    )
    origin = models.ForeignKey(
        Origin,
        on_delete=models.CASCADE,
        db_column='origin_id',
        to_field='origin_id'
    )

    class Meta:
        db_table = 'leads'

    def __str__(self):
        return self.lead_name