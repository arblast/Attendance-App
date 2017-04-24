from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def detail(request, attendee_id):
    return HttpResponse("You're looking at attendee %s" % attendee_id)
