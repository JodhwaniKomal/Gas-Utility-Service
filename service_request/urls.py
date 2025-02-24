from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet, home, submit_request, request_list, request_success  


router = DefaultRouter()
router.register(r'api/requests', ServiceRequestViewSet, basename='service-requests')

urlpatterns = [
    path("", home, name="home"),
    path("submit/", submit_request, name="submit_request"),
    path("track/", request_list, name="track_requests"),
    path("success/", request_success, name="request_success"),

]

urlpatterns += router.urls
