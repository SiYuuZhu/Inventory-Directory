from django.db import models

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    serial_num = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='images')
    quantity = models.PositiveSmallIntegerField()
    vendor_email = models.EmailField(max_length=100, unique=True)
    vendor_phone = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item_name