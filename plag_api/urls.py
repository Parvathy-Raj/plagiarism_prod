from django.urls import path
from .views import PlagDataView


app_name = 'plag_api'

urlpatterns = [
   path("PlagiarismCheck/", PlagDataView.as_view(), name ="plagiarism" )
]
