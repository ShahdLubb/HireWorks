from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


import json
from django.http import HttpResponse
from django.views.defaults import page_not_found
from HireWorks.models import Job
from HireWorks.models import Employer

def job_list(request):
    if request.method == 'GET':
        jobs = Job.objects.using('HireWorks').all()
        return jobs_details(jobs)
    else:
        return page_not_found(request, exception=Exception('Page not Found'))

def search_jobs_by_location(request, location):
    if request.method == 'GET':
        jobs = Job.objects.using('HireWorks').filter(location=location)
        return jobs_details(jobs)
    else:
        return page_not_found(request, exception=Exception('Page not Found'))

def search_jobs_by_title(request, title):
    if request.method == 'GET':
        jobs = Job.objects.using('HireWorks').filter(title=title)
        return jobs_details(jobs)
    else:
        return page_not_found(request, exception=Exception('Page not Found'))

def search_jobs_by_salary(request, salary):
    if request.method == 'GET':
        jobs = Job.objects.using('HireWorks').filter(salary__gte=salary)
        return jobs_details(jobs)
    else:
        return page_not_found(request, exception=Exception('Page not Found'))

def search_jobs_by_salary_range(request, min_salary,max_salary):
    if request.method == 'GET':
        jobs = Job.objects.using('HireWorks').filter(salary__gte=min_salary,salary__lte=max_salary)
        return jobs_details(jobs)
    else:
        return page_not_found(request, exception=Exception('Page not Found'))

def jobs_details(jobs):
    job_data = [
            {
                'company name':job.employer.company_name,
                'title': job.title,
                'description': job.description,
                'salary':"{}$".format(job.salary),
                'requirments':job.requirements,
                'location': job.location,
                'application deadline': job.deadline.strftime('%Y-%m-%d')
            }
            for job in jobs
        ]
    if(jobs.count() == 0) :
       job_data ={'message': 'no jobs found'}
    json_data = json.dumps(job_data, indent=4)
    return HttpResponse(json_data, content_type='application/json')

