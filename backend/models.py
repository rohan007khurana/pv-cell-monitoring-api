from django.db import models

# Create your models here.
class Reading(models.Model):
    v_oc = models.DecimalField(max_digits=5, decimal_places=2)
    i_sc = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']