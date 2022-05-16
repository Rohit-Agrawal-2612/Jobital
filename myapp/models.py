from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class job(models.Model):
    name = models.CharField(max_length=100)
    batch = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    brief = models.CharField(max_length=100)
    mobile = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=100)
    telephone = models.IntegerField()
    description = models.CharField(max_length=500)
    responsibilities = models.CharField(max_length=500)
    qualifications = models.CharField(max_length=500)
    about = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='company_images/')
    salary = models.IntegerField()
    type = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    currency = models.CharField(max_length=20, default='$')

class testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    testimonial = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='testimonials/')
    stars = models.IntegerField()

class contactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)

class newsLetter(models.Model):
    email = models.EmailField()

class team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='teams/')

class registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    open_to_relocate = models.CharField(max_length=10)
    resume = models.FileField(upload_to='resumes/')
    company_name = models.CharField(max_length=50)
    work_mode_preference = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='pictures/')
    notice_period = models.IntegerField(default=0)
    current_ctc = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    expected_ctc = models.IntegerField()
    status = models.CharField(max_length=50,default='under process')
    email = models.EmailField()
    area_code = models.IntegerField()

    