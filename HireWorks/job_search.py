
from django.views.defaults import page_not_found
from HireWorks.models import Job
from HireWorks.job_utility import *
from rest_framework.decorators import api_view


@api_view(['GET'])
def search_jobs_by_location(request, location):
        jobs = Job.objects.using('HireWorks').filter(location=location)
        currency="USD"
        if 'currency' in request.GET:
            currency = request.GET['currency']
        return jobs_details(jobs,currency)
   
@api_view(['GET'])
def search_jobs_by_title(request, title):
        jobs = Job.objects.using('HireWorks').filter(title=title)
        currency="USD"
        if 'currency' in request.GET:
            currency = request.GET['currency']
        return jobs_details(jobs,currency)
  
@api_view(['GET'])
def search_jobs_by_salary(request, salary):
        jobs = Job.objects.using('HireWorks').filter(salary__gte=salary)
        currency="USD"
        if 'currency' in request.GET:
            currency = request.GET['currency']
        return jobs_details(jobs,currency)
 
@api_view(['GET'])
def search_jobs_by_salary_range(request, min_salary,max_salary):
        jobs = Job.objects.using('HireWorks').filter(salary__gte=min_salary,salary__lte=max_salary)
        currency="USD"
        if 'currency' in request.GET:
            currency = request.GET['currency']
        return jobs_details(jobs,currency)
   