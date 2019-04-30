from django import forms
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

from django.utils.datetime_safe import datetime




class User(models.Model):
    f_name=models.CharField(max_length=30)
    m_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    age=models.IntegerField()
    dob =models.DateField()
    height=models.FloatField(max_length=30)
    mob_no=models.IntegerField()
    address=models.CharField(max_length=30)
    M_status=(
        ('y', 'yes'),
        ('n', 'no'),
    )
    m_status=models.CharField(max_length=1,choices=M_status)

    def __str__(self):
        return self.f_name

    class Meta:
        verbose_name_plural = "User"
        db_table = 'user'

class University(models.Model):
        University_name=models.CharField(max_length=20)
        University_address=models.CharField(max_length=20)

        def __str__(self):
            return self.University_name

        class Meta:
            verbose_name_plural = "Universities"
        #db_table = 'university'

class Academic(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    university_name=models.ForeignKey(University,on_delete=models.CASCADE)

    #academic=models.ManyToManyField(User)


    degree=models.CharField(max_length=20)
    percentage=models.FloatField()
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name_plural = "Academic"
        #db_table = 'academic'

class Company(models.Model):
    Company_name=models.CharField(max_length=30)
    Company_address=models.CharField(max_length=30)
    def __str__(self):
        return self.Company_name

    class Meta:
        verbose_name_plural = "Companies"
        #db_table = 'company'

class Experience(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    company_name=models.ForeignKey(Company,on_delete=models.CASCADE)
    #sal=models.OneToOneField(User,on_delete=models.CASCADE)

    salary=models.FloatField()
    designation=models.CharField(max_length=30)
    currrently_working=models.BooleanField()
    hire_date=models.DateField()
    end_date =models.DateField()
    date_now= datetime.today().date()

    # def clean(self):
    #     if self.end_date < self.hire_date:
    #         msg = u"End date should be greater than start date."
    #         raise ValidationError(msg)
    #     if self.end_date>self.date_now:
    #         msg = u"End date should not be greater than start date."
    #         raise ValidationError(msg)



    def __str__(self):
            return '{} {}  {}'.format(self.user_name, self.company_name,self.designation)

    class Meta:
        verbose_name_plural = "Experiencies"
        #db_table = 'experience'


