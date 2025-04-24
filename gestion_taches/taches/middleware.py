from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                request.user.userprofile
            except UserProfile.DoesNotExist:
                UserProfile.objects.create(user=request.user)

        response = self.get_response(request)
        return response 