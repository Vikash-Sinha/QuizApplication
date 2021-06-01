from .import views
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import *

urlpatterns = [
    path('add-issue', AddIssue.as_view(), name="add_issue"),
    ]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)