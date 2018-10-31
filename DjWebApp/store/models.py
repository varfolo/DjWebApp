from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
 
# Расщирение модели пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key = True)
    userPic = models.FileField(blank=True, upload_to='store/images/',default='noimage')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
          Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()