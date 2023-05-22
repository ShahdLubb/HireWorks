from rest_framework import serializers
from HireWorks.models import Job,Application

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields=('job_id','employer','title','description','salary','requirements','location','deadline')

class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields=('application_id','resume','job','candidate')