from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ServiceRequestForm
from .models import ServiceRequest
from rest_framework import viewsets
from .serializers import ServiceRequestSerializer


def home(request):
    return render(request, "home.html")

def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("request_success")  # ✅ Redirect to success page
    else:
        form = ServiceRequestForm()

    return render(request, "service_request_form.html", {"form": form})

def request_list(request):
    requests = ServiceRequest.objects.all()
    return render(request, "request_list.html", {"requests": requests})

def request_success(request):
    return render(request, "request_success.html")

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer


