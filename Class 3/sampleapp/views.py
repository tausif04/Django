from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

from .forms import TaskForm

from django.views import View


class TaskCreateView(View):
    form_class = TaskForm
    def get(self,request):
        form = self.form_class()
        context= {
            "form":form
        }
        return render(
            request,
            'task_create.html',
            context
        )
    
    def post(self,request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form submitted successfully")
        else:
            context={
                "form":form
            }
            return render(request, 'task_create.html',context)

# def form_view(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Form submitted successfully")
#         e    lse:
#             context={
#                 "form":form
#             }
#             return render(request, 'task_create.html',context)
#     return render(request, 'task_create.html',context)

