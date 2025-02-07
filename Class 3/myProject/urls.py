"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse,JsonResponse
import json
from  django.views.decorators.csrf import csrf_exempt

def home(request):
    return JsonResponse(
        {'message': "Hello, World!",
         'status': "200,OK"
         }

        )
@csrf_exempt
def methods_test(request):
    print(f"\n===Incoming {request.method} request===") #Check the type of request
    print(f"Headers: {request.headers}") #Check the URL for Headers 

    print(f"Body: {request.body}") #Check the URL for Body

    print(f"Params: {request.GET}") #Check the URL for parameters


    if request.method =='GET':
        return JsonResponse({'message': 'Reading Data'})
    elif request.method =='POST':
        # if Json
        # data =json.loads((request.body).decode('utf-8'))
        # print(data)

        # if form Data
        # data= request.POST
        # print(data) 
        if request.headers.get(("Content-Type")) == 'application/json':
            data = json.loads(request.body)
            print(data)
        else:
            data = request.POST
            files=request.FILES
            print(data)
            print(files)

        return JsonResponse({'message': 'Data Created'})    
    
    elif request.method in ['PUT', 'PATCH']:
        return JsonResponse({'message':'Data  Updated'})
    
    elif request.method == 'DELETE':
        return JsonResponse({'message':'Data Deleted'})
    return JsonResponse({'message':'Data Created'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('methods_test/', methods_test)
]
