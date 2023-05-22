from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from HireWorks.models import Job,Application,Employer
from HireWorks.serializers import JobSerializers,ApplicationSerializers


def get_next_job_id():
    next_job_id = Job.objects.using("HireWorks").all().order_by('-job_id').first().job_id + 1
    return next_job_id

def add_job(data):
     title = data.get('title')
     description = data.get('description')
     salary = data.get('salary')
     requirements = data.get('requirements')
     deadline = data.get('deadline')
     location = data.get('location')
     job_id= get_next_job_id()
     employer=Employer.objects.using("HireWorks").get(email=data.get('employer_email'))
     try:
         job = Job(job_id,employer.employer_id,title, description,salary,requirements,location,deadline)
         # save the application to the database
         job.save(using='HireWorks')
         response_data = {'success': True, 'message': "Added To Job Table Successfully"}
         return JsonResponse(response_data,safe=False, status=200)
     except Exception as e:
            # return an error response if any exception occurs
            response_data = {'success': False, 'message': str(e)}
            return JsonResponse(response_data, status=400)
def delete_job(id):
    try:
        print(id)
        job=Job.objects.using("HireWorks").get(job_id=id)
        job.delete()
        response_data = {'success': True, 'message': "Job deleted Successfully"}
        return JsonResponse(response_data,safe=False, status=200)
    except Exception as e:
            # return an error response if any exception occurs
            response_data = {'success': False, 'message': str(e)}
            return JsonResponse(response_data, status=400)
def job_details(job):
    job_data = {
                'job id': job.job_id,
                'company name':job.employer.company_name,
                'title': job.title,
                'description': job.description,
                'salary':job.salary,
                'requirments':job.requirements,
                'location': job.location,
                'application deadline': job.deadline.strftime('%Y-%m-%d')
              }
        
    json_data = json.dumps(job_data, indent=4)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def jobApi(request,id=0):
  if request.method=='GET' :
    job=Job.objects.using("HireWorks").get(job_id=id)
    return job_details(job)
  
  elif request.method=='POST':
    data = json.loads(request.body)
    return add_job(data)
    
  elif request.method=='PUT':
     job_data=JSONParser().parse(request)
     job=Job.objects.using("HireWorks").get(job_id= job_data['job_id'])
     job_serializers=JobSerializers(job,data=  job_data)
     if  job_serializers.is_valid():
       job_serializers.save()
       return JsonResponse("Update Successfully",safe=False)
     return JsonResponse("Failed To Job Table Update",safe=False)
  elif request.method=='DELETE':
    return delete_job(id)
  

@csrf_exempt
def applicaionApi(request,id=0):
  if request.method=='GET' :
    application=Application.objects.all()
    application_serializers=ApplicationSerializers(application,many=True)
    return JsonResponse(application_serializers.data,safe=False)
  elif request.method=='PUT':
     app_data=JSONParser().parse(request)
     app=Application.objects.get(application_id= app_data['application_id'])
     app_serializers=ApplicationSerializers(app,data=  app_data)
     if  app_serializers.is_valid():
         app_serializers.save()
         return JsonResponse("Update Application Table Successfully",safe=False)
     return JsonResponse("Failed To Update",safe=False)
  elif request.method=='DELETE':
    app=Application.objects.get(application_id=id)
    app.delete()
    return JsonResponse("Delete From Application Table Successfully",safe=False)
  
  def add_job(data):
     title = data.get('title')
     description = data.get('description')
     salary = data.get('salary')
     requirements = data.get('requirements')
     deadline = data.get('deadline')
     location = data.get('location')
     job_id= get_next_job_id()
     employer=Employer.objects.using("HireWorks").get(email=data.get('employer_email'))
     try:
         job = Job(job_id,employer.employer_id,title, description,salary,requirements,location,deadline)
         # save the application to the database
         job.save(using='HireWorks')
         response_data = {'success': True, 'message': "Added To Job Table Successfully"}
         return JsonResponse(response_data,safe=False, status=200)
     except Exception as e:
            # return an error response if any exception occurs
            response_data = {'success': False, 'message': str(e)}
            return JsonResponse(response_data, status=400)