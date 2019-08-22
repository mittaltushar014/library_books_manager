from testapp import views
from django.conf.urls import url
urlpatterns =[
    url('about/',views.about),
    url('showTest/',views.showContact),
    url('^$',views.greeting),
    url('employees',views.employee_info_view),
]
