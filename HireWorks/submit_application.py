from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.http import JsonResponse
from HireWorks.models import Application, Candidate, Job
from HireWorks.job_utility import *
from rest_framework.decorators import api_view

@api_view(['POST'])
@csrf_exempt
def submit_job_application(request):
    
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
    


