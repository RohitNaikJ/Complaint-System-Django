from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=40, default='Vinay Rebeiro')
    email = models.CharField(max_length=40, default='Vinay@iitd.ac.in')
    userName = models.CharField(max_length=40, default='vinay', unique=True)
    password = models.CharField(max_length=40, default='vinay')
    TYPES_OF_USERS = (
        ('Student', 'Student'),
        ('Warden', 'Warden'),
        ('Faculty', 'Faculty'),
    )
    typeOfUser = models.CharField(max_length=20, choices=TYPES_OF_USERS,
                                  default='Student')
    TYPES_OF_RESIDENCIES = (
        ('Karakoram', 'Karakoram'),
        ('Nilgiri', 'Nilgiri'),
        ('Himadri', 'Himadri'),
        ('Jwalamukhi', 'Jwalamukhi'),
        ('Udaigiri', 'Udaigiri'),
        ('Appartment', 'Appartment'),
        ('Individual', 'Individual Housing'),
    )
    residency = models.CharField(max_length=25, choices=TYPES_OF_RESIDENCIES,
                                  default='Karakoram')
    roomNo = models.CharField(max_length=40)
    contactNo = models.BigIntegerField(default=9910272880)

    def __str__(self):
        return self.userName

class AuthorityWorker(models.Model):
    name = models.CharField(max_length=40, default='Vinay Rebeiro')
    email = models.CharField(max_length=40, default='Vinay@iitd.ac.in')
    userName = models.CharField(max_length=40, default='vinay', unique=True)
    password = models.CharField(max_length=40, default='vinay')
    WORKING_AUTHORITY = (
        ('electricity', 'Electrician'),
        ('plumber', 'Plumber'),
        ('carpenter', 'Carpenter'),
        ('security', 'Security'),
        ('csc', 'Computer Services Center'),
    )
    type = models.CharField(max_length=12, choices=WORKING_AUTHORITY, default='electrician')
    contactNo = models.BigIntegerField(default=9910272880)

    def __str__(self):
        return self.userName


class Complaints(models.Model):
     title = models.CharField(max_length=200, help_text="Title of the Complaint")
     description = models.TextField(help_text='Enter Complaint Description')
     votes = models.IntegerField(default=0)
     TYPES_OF_CATOGERY = (
         ('electricity','Electricity'),
         ('plumber','Plumber'),
         ('carpentry','Carpentry'),
         ('sports','Sports'),
         ('cultural','Cultural'),
         ('library','Library'),
         ('csc','Computer Services Center'),
         ('mess','Mess'),
         ('security','Security'),
         ('others','Others'),
     )
     LEVEL_OF_COMPLAINT = (
         ('individualLevel','Individual'),
         ('hostelLevel','Hostel'),
         ('instituteLevel','Institute')
     )
     TYPES_OF_ORIGIN = (
        ('Karakoram', 'Karakoram'),
        ('Nilgiri', 'Nilgiri'),
        ('Himadri', 'Himadri'),
        ('Jwalamukhi', 'Jwalamukhi'),
        ('Udaigiri', 'Udaigiri'),
        ('Institute', 'IIT Delhi'),
        ('Individual', 'Individual House'),
     )
     complaint_roomNo = models.CharField(max_length=40, default='0', null=True, blank=True)
     origin = models.CharField(choices=TYPES_OF_ORIGIN, max_length=20, default='Karakoram')
     levelOfComplaint = models.CharField(choices=LEVEL_OF_COMPLAINT, max_length=15)
     category = models.CharField(choices=TYPES_OF_CATOGERY, default='others', max_length=15)
     createdDate = models.DateTimeField(auto_now_add=True)
     resolvedDate= models.DateField(blank=True, null=True)
     ASSIGNED_OR_UNASSIGNED = (
         (False, 'Unassigned to any authority personnel'),
         (True, 'Assigned to an authority personnel'),
     )
     RESOLVED_OR_UNRESOLVED = (
         (True, 'Complaint Resolved'),
         (False, 'Complaint yet to be Resolved')
     )
     status_AS = models.BooleanField(choices=ASSIGNED_OR_UNASSIGNED, default=False)
     status_RU = models.BooleanField(choices=RESOLVED_OR_UNRESOLVED, default=False)
     lodgedBy = models.ForeignKey(Users, on_delete= models.CASCADE)
     assignedWorker = models.ForeignKey(AuthorityWorker, on_delete=models.CASCADE, blank=True, null=True)

     def __str__(self):
         return self.title

class Comments(models.Model):
     comment_title = models.CharField(max_length=100,default='')
     comment_date = models.DateTimeField(auto_now_add=True)
     complaint = models.ForeignKey(Complaints, on_delete=models.CASCADE)
     comment_by = models.ForeignKey(Users,on_delete=models.CASCADE)
     def __str__(self):
         return self.comment_title