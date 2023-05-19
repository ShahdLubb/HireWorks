from django.db import models

# Create your models here.

class Employer(models.Model):
    employer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    company_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        db_table = 'employers'
        app_label = 'HireWorks'
    using = 'HireWorks'


class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    employer= models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.IntegerField()
    requirements = models.TextField()
    location = models.CharField(max_length=20)
    deadline = models.DateField()

    class Meta:
        db_table = 'jobs'
        app_label = 'HireWorks'
    using = 'HireWorks'


class Candidate(models.Model):
    candidate_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        db_table = 'candidates'
        app_label = 'HireWorks'
    using = 'HireWorks'


class Application(models.Model):
    application_id = models.IntegerField(primary_key=True)
    resume = models.CharField(max_length=50)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('job', 'candidate',)
        db_table = 'applications'
        app_label = 'HireWorks'
    using = 'HireWorks'

   