from django.db import models
from accounts.models import User

GENDER_CHOICES = (
        ('male' , 'Male'),
        ('female' , 'Female'),
        ('other' , 'Other')
    )

class PatientProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55, unique=True, null=True, blank=True)
    profile_pic = models.ImageField(upload_to = 'user_pro_pic', default='default/pro_pic.png')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField()
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class DoctorProfile(models.Model):

    DEPARTMENT_CHOICES = (
        ('General' , 'General'),
        ('Allergists/Immunologists' , 'Allergists/Immunologists'),
        ('Anesthesiologists' , 'Anesthesiologists'),
        ('Cardiologists' , 'Cardiologists'),
        ('ENT' , 'ENT'),
        ('Emergency Medicine Specialists' , 'Emergency Medicine Specialists'),
        ('Family Physicians' , 'Family Physicians'),
        ('General Surgeons' , 'General Surgeons'),
        ('Pediatricians' , 'Pediatricians'),
        ('OtOlaryngologist(ear)' , 'Otolaryngologist(ear)'),
        ('Ophthalmologist(eye)' , 'Ophthalmologist(eye)'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55, unique=True)
    profile_pic = models.ImageField(upload_to = 'user_pro_pic', default='default/pro_pic.png')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField()
    qualifications = models.CharField(max_length=55)
    speciality = models.CharField(max_length=100)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class NurseProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55, unique=True)
    profile_pic = models.ImageField(upload_to = 'user_pro_pic', default='default/pro_pic.png')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField()
    qualifications = models.CharField(max_length=55)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class PharmacistProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55, unique=True)
    profile_pic = models.ImageField(upload_to = 'user_pro_pic', default='default/pro_pic.png')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField()
    qualifications = models.CharField(max_length=55)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

