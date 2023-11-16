from django.db import models
from django.core.validators import FileExtensionValidator




COMPONY_SIZE = (
    ('1','1-10'),
    ('2','11-50'),
    ('3','51-200'),
    ('4','201-500'),

)

INDUSTRY = (
    ('1','Aggriculture'),
    ('2','Banking&Finance'),
    ('3','Bussiness Services & Softweare'),
    
)

JOB_ROLE = (
    ('1','C-Suite'),
    ('2','VP')
    
)

COUNTRY = (
    ('1','Bangladesh'),
    ('2','China'),
    ('3','India'),
    ('4','Japan'),
    ('5','United States'),

)



# Create your models here.
class Creators(models.Model):
    product = models.ForeignKey("web.Solution", on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True, null=True)
    files_image = models.FileField(upload_to="testimonials/")

    white_image = models.FileField(upload_to="testimonials/",blank=True,null=True)


   
class Subscribe(models.Model):
    # (unique=True) 1 mail 1 pravashyam use chayyan kayiyum
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.email
    
class Futiuersection(models.Model):
    image = models.ImageField(upload_to="testimonials/")
    icon = models.FileField(upload_to="testimonials/")
    icon_background = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_auter = models.CharField(max_length=250)
    auther_designation = models.CharField(max_length=250)
    testimonial_logo = models.FileField(upload_to="testimonials/")

    def __str__(self):
        return self.title

class Creatvedeo(models.Model):
    image = models.ImageField(upload_to="testimonials/")
    icon = models.FileField(upload_to="testimonials/")
    description = models.TextField()


class Partners(models.Model):
    image = models.ImageField(upload_to="testimonials/")
    icon = models.FileField(upload_to="testimonials/")
    description = models.TextField()
    auther = models.CharField(max_length=250)
    auther_designation = models.CharField(max_length=250)
    field = models.CharField(max_length=250)

    def __str__(self):
        return self.auther


class Marketting(models.Model):
    image = models.FileField(upload_to="testimonials/")
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class Solution(models.Model):
    logo = models.FileField()
    title = models.CharField(max_length=250)
    her_image = models.ImageField(upload_to="testimonials/")
    name = models.CharField(max_length=128)
    description = models.TextField()
    color = models.CharField(max_length=128)
    button_color =models.CharField(max_length=250)
    backgroun = models.CharField(max_length=250)
    image = models.ImageField(upload_to="testimonials/")

    class Meta:
        db_table = "web_product"
        ordering = ["id"]

    def __str__(self):
        return self.title


class Resources(models.Model):
    image = models.ImageField(upload_to="testimonials/")
    title = models.CharField(max_length=250)
    title_color = models.CharField(max_length=250,blank=True, null=True)
    description = models.TextField()
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    compony = models.CharField(max_length=128)
    compony_size = models.CharField(max_length=128,choices=COMPONY_SIZE)
    indutry = models.CharField(max_length=128,choices=INDUSTRY)
    job_role = models.CharField(max_length=128,choices=JOB_ROLE)
    country = models.CharField(max_length=128,choices=COUNTRY)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table = "web_contact"
        ordering = ["-id"]

    def __str__(self):
        return self.first_name
            