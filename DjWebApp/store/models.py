from django.db import models

# Модель создаваемого пользователем продукта
class UserProduct(models.Model):
   # productId = models.AutoField(unique=True)
    userId = models.BigIntegerField()
    productName = models.CharField(null=False, max_length=50)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    Category = models.CharField(max_length=20)
    image = models.FileField()
    CreateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName
    