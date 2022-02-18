from django.urls import path

from navigator import views

urlpatterns = [
    path("get-route/", views.GetRouteAPIView.as_view()),
    path("plan-route/", views.PlanRouteAPIView.as_view())
]
