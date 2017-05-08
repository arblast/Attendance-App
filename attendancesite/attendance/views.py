from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Attendee
from .models import AttendanceDay
from forms.attendee_form import AttendeeForm

def index(request):
    attendee_list = Attendee.objects.all()
    context = {'attendee_list': attendee_list}
    return render(request, 'attendance/index.html', context)

def detail(request, attendee_id):
    attendee = get_object_or_404(Attendee, id = attendee_id)
    context = {'attendee': attendee}
    return render(request, 'attendance/detail.html', context)

def edit(request, attendee_id):
    attendee = get_object_or_404(Attendee, id = attendee_id)
    if request.method == 'GET':
        form = AttendeeForm(initial={'first_name': attendee.first_name, 'last_name': attendee.last_name, 'group': attendee.group})
        return render(request, 'attendance/edit.html', {'attendee': attendee, 'form': form})
    elif request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee.first_name = form.cleaned_data['first_name']
            attendee.last_name = form.cleaned_data['last_name']
            attendee.group = form.cleaned_data['group']
            attendee.save()
            return HttpResponseRedirect(reverse('attendance:detail', args=(attendee.id,)))

def add(request, attendee_id):
    year = request.POST['year']
    month = request.POST['month']
    day = request.POST['day']
    date = datetime.date(year, month, day)
    attendanceday = AttendanceDay.create(date=date, attendee_id=attendee_id)
    attendanceday.save()
    return HttpResponseRedirect(reverse('attendance:detail', args=(attendee.id,)))
