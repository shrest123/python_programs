from django.db import models
from django.utils import timezone
from django .contrib.auth.models import User

# Create your models here.
class Test_list(models.Model):
    name = models.CharField(max_length=50 )
    created_id=models.DateTimeField(default=timezone.now() )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
      return f"{self.name} ----{self.created_id}" 



class Test(models.Model):
    name = models.CharField(max_length=50 )
    desc = models.TextField()
    created_at = models.DateTimeField(default=timezone.now() )
    due_date =   models.DateTimeField()
    name_2 = models.CharField(max_length=50 )
    list=models.ForeignKey(Test_list,on_delete=models.CASCADE)
    def  __str__(self):
      return f"{self.name} ----{self.desc}"


  