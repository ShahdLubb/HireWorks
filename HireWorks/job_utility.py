from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.views.defaults import page_not_found
from HireWorks.models import Application, Candidate, Job
from HireWorks.models import Employer
from HireWorks.exchange import exchange_amount

def jobs_details(jobs,currency):
    job_data = [
            {
                
                'job id': job.job_id,
                'company name':job.employer.company_name,
                'title': job.title,
                'description': job.description,
                'salary':format_salary(job.salary,currency),
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

def format_salary(salary,currency):
    if currency != "USD":
        NewSalary=exchange_amount(currency,salary)
        if NewSalary == None:
            currency="USD"
        else: 
           salary=NewSalary

    return "{} {}".format(salary,currency)