from django.db import models

class Futsal(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    price = models.IntegerField()
    phone = models.IntegerField()
    About = models.TextField(max_length=500, null = True)

    def __str__(self):
        return self.name

    
class FutsalProfile(models.Model):
    futsal = models.OneToOneField(Futsal, on_delete=models.CASCADE)
    Available=models.CharField(max_length=10)
    profile_picture = models.FileField(null=True, blank= True, upload_to="profile_pictures")


