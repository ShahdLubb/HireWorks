from django.shortcuts import render

# Create your views here.


import json
from django.http import HttpResponse
from HireWorks.models import Job
from HireWorks.models import Employer

def job_list(request):
    jobs = Job.objects.using('HireWorks').all()
    
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
    json_data = json.dumps(job_data, indent=4)
    return HttpResponse(json_data, content_type='application/json')

