from django.shortcuts import render
from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe

from .models import Event
from .utils import Calendar
# Create your views here.

def home(request):
    return render(request, 'calendar_app/home.html')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar_app/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('day', None))

        #Init calendar 
        cal = Calendar(d.year, d.month)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()