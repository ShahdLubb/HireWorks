
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.views.defaults import page_not_found
from HireWorks.models import Application, Candidate, Job
from HireWorks.models import Employer
from HireWorks.exchange import exchange_amount
from HireWorks.job_utility import *

def search_jobs_by_location(request, location):
    if request.method == 'GET':
        jobs = Job.objects.using('HireWorks').filter(location=location)
        currency="USD"
        if 'currency' in request.GET:
            currency = request.GET['currency']
        return jobs_details(jobs,currency)
    else:
        return page_not_found(request, exception=Exception('Page not Found'))

def search_jobs_by_title(request, title):
    if request.method == 'GET':
        jobs = Job.objects.using('HireWorks').filter(title=title)
        currency="USD"
        if 'currency' in request.GET:
            currency = request.GET['currency']
        return jobs_details(jobs,currency)
    else:
        return page_not_found(request, exception=Exception('Page not Found'))

def search_jobs_by_salary(request, salary):
    if request.method == 'GET':
        jobs = Job.objects.using('HireWorks').filter(salary__gte=salary)
        currency="USD"
        if 'currency' in request.GET:
            currency = request.GET['currency']
        return jobs_details(jobs,currency)
    else:
        return page_not_found(request, exception=Exception('Page not Found'))

def search_jobs_by_salary_range(request, min_salary,max_salary):
    if request.method == 'GET':
        jobs = Job.objects.using('HireWorks').filter(salary__gte=min_salary,salary__lte=max_salary)
        currency="USD"
        if 'currency' in request.GET:
            currency = request.GET['currency']
        return jobs_details(jobs,currency)
    else:
        return page_not_found(request, exception=Exception('Page not Found'))
