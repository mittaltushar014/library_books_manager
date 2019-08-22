from exam import views
from django.conf.urls import url
urlpatterns =[
    url('showTest/',views.showTest),
    url('showResult/',views.showResult),
]
