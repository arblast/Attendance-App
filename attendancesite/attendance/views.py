from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Attendee


def index(request):
    attendee_list = Attendee.objects.all()
    context = {'attendee_list': attendee_list}
    return render(request, 'attendance/index.html', context)

def detail(request, attendee_id):
    attendee = get_object_or_404(Attendee, id = attendee_id)
    context = {'attendee': attendee}
    return render(request, 'attendance/detail.html', context)
