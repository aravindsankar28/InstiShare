from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

HOSTEL_CHOICES  =(
        ("Ganga", "Ganga"),
        ("Mandak", "Mandak"),
        ("Jamuna", "Jamuna"),
        ("Alak", "Alak"),
        ("Saraswathi", "Saraswathi"),
        ("Narmada", "Narmada"),
        ("Godav", "Godav"),
        ("Pampa", "Pampa"),
        ("Tambi", "Tambi"),
        ("Sindhu", "Sindhu"),
        ("Mahanadi", "Mahanadi"),
        ("Sharavati", "Sharavati"),
        ("Krishna", "Krishna"),
        ("Cauvery", "Cauvery"),
        ("Tapti", "Tapti"),
        ("Brahmaputra", "Brahmaputra"),
        ("Sarayu", "Sarayu"),
 		("DS","DS")
        )


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    nick = models.CharField(max_length = 20,blank = True) 
    phone_number = models.CharField(max_length = 15, blank = False)
    email = models.EmailField(max_length = 50)
    hostel = models.CharField(max_length = 20,choices=HOSTEL_CHOICES)
    
# Create your models here.
