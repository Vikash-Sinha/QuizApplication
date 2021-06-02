from .import views
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import *

urlpatterns = [
    # path('view-list', QuizList.as_view(), name="quiz_list"),
    path('', QuizList.as_view(), name="quiz_list"),
    # path('add-issue', AddIssue.as_view(), name="add_issue"),
    ]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)