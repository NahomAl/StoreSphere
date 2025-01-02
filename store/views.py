from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def dashboard_callback(request, context):
    # Fetch dynamic data here, e.g., counts or statistics
    context.update({
        "custom_variable": "Hello, Dashboard!",
        "user_count": User.objects.count(),  # Example of fetching user data
    })
    return context
