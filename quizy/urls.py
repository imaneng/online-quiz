
from django.urls import path

from .views import *


urlpatterns = [
    
    path("show_q/",show_question ),
    path("ans/",get_answer),
    path("user",get_user),
    path('result',show_score)
]