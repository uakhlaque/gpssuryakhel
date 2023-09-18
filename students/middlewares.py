from django.http import HttpResponseRedirect
from django.urls import reverse

class StudentsAppAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'students/' in request.path and not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return self.get_response(request)
