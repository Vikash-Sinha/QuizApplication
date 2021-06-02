from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib import messages
from djqscsv import render_to_csv_response
from django.core.mail import send_mail
from QuizApplication.settings import *
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

class QuizList(View):
    template = 'Quiz/quiz_list.html'
    def get(self,request):
        if request.META['SERVER_PORT'] =='8001':
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

        else:
            return redirect('add_issue')

    def post(self,request):
        pass
