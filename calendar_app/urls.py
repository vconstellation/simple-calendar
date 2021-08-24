from django.conf.urls import url
from .views import home, CalendarView, event

app_name = 'cal'
urlpatterns = [
    url('home/', home, name='home-page'),
    url(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    url('event/new/', event, name='event-new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', event, name='event-edit'),
]