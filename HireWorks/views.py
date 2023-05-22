from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.views.defaults import page_not_found
from HireWorks.models import Application, Candidate, Job
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

@csrf_exempt
def submit_job_application(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            job_id = data.get('job_id')
            email = data.get('email')
            resume = data.get('resume')
            
            # get the job and candidate who is applying
            job = Job.objects.using("HireWorks").get(job_id=job_id)
            candidate = Candidate.objects.using("HireWorks").get(email=email)

            #check the job deadline
            CurrentDate = datetime.date.today()
            if(job.deadline < CurrentDate):
                response_data = {'success': False, 'message': ' job application deadline has already passed'}
                return JsonResponse(response_data)
            # create the application object
            next_application_id = Application.objects.using("HireWorks").all().order_by('-application_id').first().application_id + 1
            application = Application(application_id=next_application_id,resume=resume, job=job, candidate=candidate)

            # save the application to the database
            application.save(using='HireWorks')

            # return a success response
            response_data = {'success': True, 'message': 'Application submitted successfully'}
            return JsonResponse(response_data)
        except Exception as e:
            # return an error response if any exception occurs
            response_data = {'success': False, 'message': str(e)}
            return JsonResponse(response_data, status=400)
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

