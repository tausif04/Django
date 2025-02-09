from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

from .forms import TaskForm

form=TaskForm()
context={
        'myform':form,
    }


def form_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form submitted successfully")
        else:
            context['myform']=form
            return render(request, 'form.html',context)
    return render(request, 'form.html',context)

