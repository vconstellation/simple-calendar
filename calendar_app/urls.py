from django.conf.urls import url
from .views import home, CalendarView

urlpatterns = [
    url('home/', home, name='home-page'),
    url('calendar/', CalendarView.as_view(), name='calendar'),
]