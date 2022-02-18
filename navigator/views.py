from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from adventure import models, notifiers, repositories, serializers, usecases


class GetRouteAPIView(generics.GenericAPIView):
    def post(self, request: Request):
        payload = request.data
        if "from_station" in payload and "to_station" in payload:
            initial_station = models.ServiceArea.objects.get(kilometer=payload["from_station"])
            final_station = models.ServiceArea.objects.get(kilometer=payload["to_station"])
            initial_station_distance_to_root = get_route_to_root(initial_station)
            final_station_distance_to_root = get_route_to_root(final_station)
            result = filter_by_conditions(initial_station, final_station, initial_station_distance_to_root, final_station_distance_to_root)

            return Response(
                {
                    "Route": result
                },
                status=200,
            )
        return Response(
                {
                    "Error": "from_station and to_station are mandatory"
                },
                status=400,
            )

class PlanRouteAPIView(generics.GenericAPIView):
    def post(self, request: Request):
        payload = request.data
        if "from_station" in payload and "to_station" in payload and "number_plate" in payload:
            vehicle = get_vehicle(payload["number_plate"])
            initial_station = models.ServiceArea.objects.get(kilometer=payload["from_station"])
            final_station = models.ServiceArea.objects.get(kilometer=payload["to_station"])
            initial_station_distance_to_root = get_route_to_root(initial_station)
            final_station_distance_to_root = get_route_to_root(final_station)
            route = filter_by_conditions(initial_station, final_station, initial_station_distance_to_root, final_station_distance_to_root)
            route_total_kilometers = get_total_kilometers(route)
            initial_vehicle_autonomy = vehicle.fuel_tank_size * vehicle.fuel_efficiency
            
            if initial_vehicle_autonomy > route_total_kilometers:
                return Response(
                {
                    "route": route,
                    "total_route_distance": route_total_kilometers,
                    "vehicle_autonomy_with_full_tank": initial_vehicle_autonomy,
                    "refuel": "no need to refuel"
                },
                status=200,
            )
                
            return Response(
                {
                    "route": route,
                    "total_route_distance": route_total_kilometers,
                    "vehicle_autonomy_with_full_tank": initial_vehicle_autonomy,
                    "refuel": "need to refuel"
                },
                status=200,
            )
        return Response(
                {
                    "Error": "from_station, to_station and number_plate are mandatory"
                },
                status=400,
            )

def get_total_kilometers(route):
    idx = 0
    counting_km = 0
    while idx < len(route):
        if idx < (len(route)-1):
            if route[idx] < route[idx + 1] and (idx + 1) != len(route):
                counting_km = counting_km + (route[idx + 1] - route[idx])
            if route[idx] > route[idx + 1] and (idx + 1) != len(route):
                counting_km = counting_km + (route[idx] - route[idx + 1])
        idx += 1
    return counting_km
    
def get_vehicle(number_plate):
    try:
        return models.Vehicle.objects.get(number_plate=number_plate)
    except models.Vehicle.DoesNotExist as e:
        raise ValidationError({"error": str(e)})

def get_route_to_root(target_station):
    current_station = get_root_station()
    route = [current_station.kilometer]
    while current_station.kilometer != target_station.kilometer:
        if target_station.kilometer > current_station.kilometer:
            current_station = models.ServiceArea.objects.get(pk=current_station.right_station_id)
        else:
            current_station = models.ServiceArea.objects.get(pk=current_station.left_station_id)
        route.append(current_station.kilometer)
    return route

def filter_by_conditions(initial_station, final_station, initial_route, final_route):
    common_elements = list(set(initial_route).intersection(set(final_route)))
    sorted_common_elements = sorted(common_elements)
    root_station = get_root_station()
    if initial_station.kilometer < root_station.kilometer and final_station.kilometer < root_station.kilometer:
        for idx, element in enumerate(sorted_common_elements):
            if element in initial_route and idx > 0:
                initial_route.remove(element)
                final_route.remove(element)
            elif element in initial_route and idx <= 0:
                initial_route.remove(element)
                
    elif initial_station.kilometer > root_station.kilometer and final_station.kilometer > root_station.kilometer:
        for idx, element in enumerate(sorted(sorted_common_elements, reverse=True)):
            if element in initial_route and idx > 0:
                initial_route.remove(element)
                final_route.remove(element)
            elif element in initial_route and idx <= 0:
                initial_route.remove(element)
    else:
        for element in initial_route:
            if element in final_route:
                final_route.remove(element)

    return initial_route[::-1] + final_route

def get_root_station():
    left_stations = models.ServiceArea.objects.values_list("left_station_id", flat=True).distinct()
    right_stations = models.ServiceArea.objects.values_list("right_station_id", flat=True).distinct()
    united_stations = left_stations.union(right_stations)
    all_stations = models.ServiceArea.objects.values_list("id", flat=True)
    root_station_id = list(set(all_stations) - set(united_stations))
    return models.ServiceArea.objects.get(pk=root_station_id[0])
