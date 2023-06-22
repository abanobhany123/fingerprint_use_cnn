from django.db import models
from datetime import datetime
# Create your models here.
 
class Finger(models.Model):

    x=[
     
      ('id','id'),
      ('name','name')

] 
   
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photos/%y/%m/%d',blank=True,null=True)
    age=models.CharField(max_length=100,default='age')
    phone=models.CharField(max_length=100,default='phone')
    adress=models.CharField(max_length=100,default='adress')
    datetime=models.DateTimeField(default=datetime.now,)
    activ=models.BooleanField(default=True )
    category=models.CharField(max_length=100,blank=True,null=True,choices=x)


    def __str__(self):
        return self.name
    class Meta:
        ordering=['id']

class Image(models.Model):
     finger=models.ForeignKey(Finger ,on_delete=models.CASCADE,related_name="finger")
    





