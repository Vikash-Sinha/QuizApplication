from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from .models import *
from django.contrib import messages
from django.http import JsonResponse
import datetime
from djqscsv import render_to_csv_response

from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import Group
from QuizApplication.settings import *
def mail_send_fun(request, subject, to_email, name):
    message = 'New Issue has been added by ' + name
    if subject and message:
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=EMAIL_HOST_USER,
                recipient_list=[to_email],
            )
        except:
            messages.success(request, "Invalid header found")
class QuizList(View):
    template = 'Quiz/quiz_list.html'
    def get(self,request):
        obj = Quizs.objects.all().order_by('-pk')
        name = request.GET.get('name')
        gender = request.GET.get('gender')
        issue = request.GET.get('issue')
        if name is not None and name is not'':
            obj = obj.filter(name__icontains=name)
        if gender is not None and gender is not'':
            obj = obj.filter(gender__icontains=gender)

        if issue is not None and issue is not'':
            obj = obj.filter(issue__icontains=issue)

        if request.GET.get('down') == 'down':
            obj = obj.values('id','name','gender','issue','img')
            return render_to_csv_response(obj)
        context = {
            'quiz_data':obj,
            'total':obj.count(),
            'name':name,
            'gender':gender,
            'issue':issue,
        }
        return render(request, self.template,context)

    def post(self,request):
        pass

class AddIssue(View):
    template = 'Quiz/add_issue.html'
    def get(self,request):
        return render(request, self.template)
    def post(self,request):
       obj = Quizs()
       obj.name = request.POST.get('name')
       obj.issue = request.POST.get('issue')
       obj.gender = request.POST.get('gender')
       obj.img = request.FILES.get('file')
       obj.save()
       mail_send_fun(request, 'New Issue Added', 'vikashsinha0rns@gmail.com', request.POST.get('name'))
       return redirect('quiz_list')