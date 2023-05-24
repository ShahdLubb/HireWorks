from HireWorks.models import Job
from HireWorks.job_utility import *
from rest_framework.decorators import api_view

@api_view(['GET'])
def job_list(request):
        jobs = Job.objects.using('HireWorks').all()
        currency="USD"
        if 'currency' in request.GET:
            currency = request.GET['currency']
        return jobs_details(jobs,currency)
    