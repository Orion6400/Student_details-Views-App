from django.db import models

class student_data(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True,blank=True)
    Address_1 = models.CharField(max_length=255)
    Address_2 = models.CharField(max_length=255)
    Guardian_Cell_phone = models.CharField(max_length=255)
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    class Meta:
        ordering = ['id']

class student_school_data(models.Model):
    student = models.ForeignKey(student_data,on_delete=models.CASCADE,related_name='school_detail')
    c_class = models.IntegerField()
    Percentage = models.DecimalField(max_digits=4,decimal_places=2)
    Commute = models.BooleanField(default=0,blank=True,null=True)

    class Meta:
        ordering = ['id']
