from django.db import models

# Create your models here.
class Stock(models.Model):
    category = models.CharField(max_length=50, blank=False, null=True)
    item_name = models.CharField(max_length=50, blank=False, null=True)
    quantity = models.IntegerField(default=0, blank=False, null=True)
    receive_quantity = models.IntegerField(default=0, blank=True, null=True)
    receive_by = models.IntegerField(blank=True, null=True)
    issue_quantity = models.IntegerField(default=0, blank=True, null=True)
    issue_by = models.IntegerField(blank=True, null=True)
    issue_to = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name + ' ' + str(self.quantity)
