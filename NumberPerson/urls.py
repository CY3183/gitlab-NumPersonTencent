from django.urls import re_path as url

from NumberPerson.views import DataView

urlpatterns = [
    url('number/person', DataView.as_view()),
]