from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from Apps.Quiz.models import *
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import Group
from QuizApplication.settings import *
from django.urls import resolve
from django.http import Http404
def mail_send_fun(request, subject, to_email, name,gender):
    message = 'New Issue has been added by ' + name + " and " + gender
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


class AddIssue(View):
    template = 'Quiz/add_issue.html'
    def get(self,request):
        if request.META['SERVER_PORT'] =='8000':
            return render(request, self.template)
        else:
            return redirect('quiz_list')
    def post(self,request):
       obj = Quizs()
       obj.name = request.POST.get('name')
       obj.issue = request.POST.get('issue')
       obj.gender = request.POST.get('gender')
       obj.img = request.FILES.get('file')
       obj.save()
       # mail_send_fun(request, 'New Issue Added', 'vikashsinha0rns@gmail.com', request.POST.get('name'),request.POST.get('gender'))

       if request.POST.get('gender') == 'Male':
           mail_send_fun(request, 'New Issue Added', 'vikashsinha0rns@gmail.com', request.POST.get('name'),
                        "hello this is male")
       elif request.POST.get('gender') == 'Female':
           mail_send_fun(request, 'New Issue Added', 'vikashsinha0rns@gmail.com', request.POST.get('name'),
                        "hello this is female")
       elif request.POST.get('gender') == 'Transgender':
           mail_send_fun(request, 'New Issue Added', 'vikashsinha0rns@gmail.com', request.POST.get('name'), "hello this is Transgender")
       return redirect('quiz_list')