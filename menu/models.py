from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/menu_images/', default='static/menu_images/brik.png')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "menu"
