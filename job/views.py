from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job

# Create your views here.

def jobs_list(request):
    jobs_list = Job.objects.all()
    paginator = Paginator(jobs_list,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj,"jobs_count":jobs_list.count()}
    return render(request,'job/jobs_list.html',context)

def job_details(request,id):
    job_details = Job.objects.get(id=id) 
    context = {'job':job_details}
    return render(request,'job/job_details.html',context)
