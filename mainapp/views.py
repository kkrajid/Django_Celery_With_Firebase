# from django.shortcuts import render,HttpResponse
# from.task import test_func
# def test(request):
#     test_func.delay()
#     return HttpResponse("Done")



from django.shortcuts import HttpResponse
from .task import read_and_notify_task

def test_view(request):
    read_and_notify_task.delay()
    return HttpResponse("Celery task triggered.")