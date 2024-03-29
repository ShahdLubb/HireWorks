"""
URL configuration for job_board_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from HireWorks.job_search import *
from HireWorks.job_listing import *
from HireWorks.submit_application import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', job_list, name='job_list'),
    path('jobs/<str:id>', jobApi),
    path('application/<str:id>',applicaionApi),
    path('jobs/location/<str:location>/', search_jobs_by_location),
    path('jobs/title/<str:title>/', search_jobs_by_title),
    path('jobs/salary/<str:salary>/', search_jobs_by_salary),
    path('jobs/salary/<str:min_salary>/<str:max_salary>/', search_jobs_by_salary_range),
    path('jobs/apply/', submit_job_application),
]
