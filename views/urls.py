from django.urls import path, include
from views.views import *

urlpatterns = [
    path('', get_review_list, name='reviews'),
    path('review/', get_review_form, name='review-form'),
]
