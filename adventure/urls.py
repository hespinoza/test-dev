from django.urls import path

from adventure import views

urlpatterns = [
    path("create-vehicle/", views.CreateVehicleAPIView.as_view()),
    path("create-service-area/", views.CreateServiceAreaAPIView.as_view()),
    path("get-service-areas/", views.GetServiceAreasAPIView.as_view()),
    path("get-service-areas-by-kilometer/<int:kilometer>", views.GetServiceAreasByKilometerAPIView.as_view()),
    path("start/", views.StartJourneyAPIView.as_view()),
    path("get-vehicles/", views.GetVehiclesAPIView.as_view()),
    path("get-vehicles-by-number-plate/<str:number_plate>", views.GetVehicleByNumberPlateAPIView.as_view()),
]
