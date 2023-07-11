from django.urls import path

from .views import seller_intake_survey, seller_intake_survey_list

urlpatterns = [
    # path("", index, name="index"),
    path('', seller_intake_survey, name='intake_survey'),
    path('results', seller_intake_survey_list, name='intake_survey_result'),
]
