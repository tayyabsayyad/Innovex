from django.db import models
from datetime import datetime


DEPT_CHOICES = (
    ('it','IT'),
    ('comps', 'COMPS'),
    ('extc','EXTC'),
    ('mech','MECH'),
)

CATEGORY_CHOICES = (
    ('PRODUCT DEVELOPMENT','PRODUCT DEVELOPMENT'),
    ('RESEARCH BASED', 'RESEARCH BASED'),
    ('SUSTAINABILITY','SUSTAINABILITY'),
    ('EMERGING TECHNOLOGY','EMERGING TECHNOLOGY'),
    ('COMMUNITY WELFARE','COMMUNITY WELFARE'),
)

DESIGNATION_CHOICES = (
    ('STUDENT','STUDENT'),
    ('FACULTY','FACULTY'),
    ('ALUMNI','ALUMNI'),
    ('PARENTS','PARENTS'),
    ('GUEST','GUEST'),
)

# Create your models here.
class Project(models.Model):
    proj_id          = models.AutoField(primary_key=True)
    proj_title       = models.CharField(max_length=100)
    proj_category    = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='PRODUCT DEVELOPMENT')
    dept             = models.CharField(max_length=6, choices=DEPT_CHOICES, default='it')
    mem1_name        = models.CharField(max_length=100,default="0")
    mem2_name        = models.CharField(max_length=100,default="0")
    mem3_name        = models.CharField(max_length=100,default="0")
    mem4_name        = models.CharField(max_length=100,default="0")
    mem1_linkedin    = models.CharField(max_length=100,default="0")
    mem2_linkedin    = models.CharField(max_length=100,default="0")
    mem3_linkedin    = models.CharField(max_length=100,default="0")
    mem4_linkedin    = models.CharField(max_length=100,default="0")
    youtube_link     = models.CharField(max_length=100,default="0")
    drive_link       = models.CharField(max_length=100,default="0")
    proj_description = models.TextField()
    tech_aspects     = models.CharField(max_length=100, default="img.jpg")
    proj_thumbnail   = models.CharField(max_length=100, default="img.jpg")

    def __str__(self):
        return str(self.proj_title)


class UserModel(models.Model):
    user_id          = models.AutoField(primary_key=True)
    user_name        = models.CharField(max_length=100)
    user_email       = models.CharField(max_length=100,unique=True)
    user_designation = models.CharField(max_length=50,choices=DESIGNATION_CHOICES, default='STUDENT')
    organisation     = models.CharField(max_length=100,default="DBIT")
    user_dept        = models.CharField(max_length=100,default="IT")
    user_year        = models.CharField(max_length=100,default="TE")

    def __str__(self):
        return str(self.user_name)


class Feedback(models.Model):
    project_dept  = models.CharField(max_length=50,choices=DEPT_CHOICES,default="IT")
    project_f     = models.ForeignKey(Project, on_delete=models.CASCADE)
    rating        = models.IntegerField()
    user_feedback = models.TextField()
    user_f        = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    user_role     = models.CharField(max_length=50,default="STUDENT")
    org_name      = models.CharField(max_length=100,default="DBIT") 
    feedback_time = models.DateTimeField(default=datetime.now)
    
    

    def __str__(self):
        return str(self.project_f)
    

