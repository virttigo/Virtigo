from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Sponsored(models.Model):
    title = models.CharField(max_length=150)
    month = models.CharField(max_length=20)
    date = models.IntegerField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    full_decription = models.TextField()
    shared = models.ManyToManyField(User, default=None, blank=True, related_name='shared')

    def __str__(self):
        return str(self.title)

    @property
    def num_shares(self):
        return self.shared.all().count() 

LIKE_CHOICES = (
    ('Earn' , 'Earn'),
    ('Forfeit' , 'Forfeit')

)

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Sponsored, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default = 'Earn', max_length=10)
    

    def __str__(self):
        return str(self.post)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.IntegerField()
    tasks_completed =models.IntegerField(null=True)
    referrals = models.IntegerField(null=True)
    subcription =models.IntegerField(null=True)
    revenue = models.IntegerField()
    notif = models.TextField(null=True)
    
    SUB_CHOICES = (
        ('Personal', 'Personal $1.99'),
        ('Business', 'Business $13'),
        ('Ultimate', 'Ultimate $39'),
        ('Premium', 'Premium $65'),
    )
    sub = models.CharField(max_length=10, choices=SUB_CHOICES)
    

   

   
    def __str__(self):
        return self.user.username

   
    

    
    

    


