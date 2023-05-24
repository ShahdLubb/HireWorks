from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from HireWorks.models import Job,Application
from HireWorks.serializers import JobSerializers,ApplicationSerializers

# Create your views here.
@csrf_exempt
def jobApi(request,id=0):
  if request.method=='GET' :
    job=Job.objects.all()
    job_serializers=JobSerializers(job,many=True)
    return JsonResponse(job_serializers.data,safe=False)
  elif request.method=='POST':
    job_data=JSONParser().parse(request)
    job_serializers=JobSerializers(data=job_data)
    if job_serializers.is_valid():
       job_serializers.save()
       return JsonResponse("Added To Job Table Successfully",safe=False)
    return JsonResponse("Failed To Add",safe=False)
    
  elif request.method=='PUT':
     job_data=JSONParser().parse(request)
     job=Job.objects.get(job_id= job_data['job_id'])
     job_serializers=JobSerializers(job,data=  job_data)
     if  job_serializers.is_valid():
       job_serializers.save()
       return JsonResponse("Update Successfully",safe=False)
     return JsonResponse("Failed To Job Table Update",safe=False)
  elif request.method=='DELETE':
    job=Job.objects.get(job_id=id)
    job.delete()
    return JsonResponse("Delete From Job Table Successfully",safe=False)
  

@csrf_exempt
def applicaionApi(request,id=0):
  if request.method=='GET' :
    application=Application.objects.all()
    application_serializers=ApplicationSerializers(application,many=True)
    return JsonResponse(application_serializers.data,safe=False)
  elif request.method=='POST':
    app_data=JSONParser().parse(request)
    app_serializers=ApplicationSerializers(data=app_data)
    if app_serializers.is_valid():
       app_serializers.save()
       return JsonResponse("Added To Application Table Successfully",safe=False)
    return JsonResponse("Failed To Add",safe=False)
    
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