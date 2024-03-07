from django.urls import path
from  django.views.generic import TemplateView

app_name = 'plag'

urlpatterns = [
    path('', TemplateView.as_view(template_name="plag/index.html")),
]

