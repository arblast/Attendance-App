from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Attendee


def index(request):
    attendee_list = Attendee.objects.all()
    context = {'attendee_list': attendee_list}
    return render(request, 'attendance/index.html', context)

def detail(request, attendee_id):
    attendee = get_object_or_404(Attendee, id = attendee_id)
    context = {'attendee': attendee}
    return render(request, 'attendance/detail.html', context)

def edit(request, attendee_id):
    print(request)
    attendee = get_object_or_404(Attendee, id = attendee_id)
    try:
        attendee.first_name = request.POST['first_name']
        attendee.last_name = request.POST['last_name']
    except (KeyError):
        return render(request, 'attendance/detail.html', {
        'attendee': attendee,
        'error_message': "You didn't enter a name.",
        })
    else:
        attendee.save()
        return HttpResponseRedirect(reverse('attendance:detail', args=(attendee.id,)))
