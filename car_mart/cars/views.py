from django.shortcuts import render
from .models import Carcompany, CEO, CarModel, FuelType
from django.db.models import Prefetch
# Create your views here.
# def Home(request):
#     car_models = CarModel.objects.all()
#     car_details = []
#     for car in car_models:  
#         car_details.append({
#            'car_name' : car.name,
#            'car_company': car.carcompany.name,
#            'CEO_name': CEO.objects.filter(carcompany= car.carcompany).first().name if CEO.objects.filter(carcompany= car.carcompany).exists() else 'N/A',
#            'Fuel_Name': [fuel.name for fuel in FuelType.objects.filter(carmodels= car)]
#         })
#     return render(request, 'cars/home.html', {'car_details': car_details})




#Optimized View using select_related and prefetch_related
def Home(request):
    car_models = CarModel.objects.select_related('carcompany').prefetch_related(
        Prefetch('carcompany__ceo'),
        Prefetch('fueltype_set')
    )
    car_details = []
    for car in car_models:  
        car_details.append({
           'car_name' : car.name,
           'car_company': car.carcompany.name,
           'CEO_name': car.carcompany.ceo.name ,
           'Fuel_Name': [fuel.name for fuel in car.fueltype_set.all()]
        })
    return render(request, 'cars/home.html', {'car_details': car_details})



  

