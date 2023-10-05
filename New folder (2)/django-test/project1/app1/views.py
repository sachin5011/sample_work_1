from django.shortcuts import render
from django.http import HttpResponse


from django.http import HttpResponse
from app1.models import appModel

def home(request):
    return render(request, "index.html")

def testmodel(request):
    data = appModel.objects.all()
    lst = []
    for d in data:
        print(d)
        d_dict = {}
        d_dict["name"] = d.name
        d_dict['age'] = d.age
        lst.append(d_dict)

    return HttpResponse(f"<h1>{lst}</h1>")
