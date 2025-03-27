import datetime


from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "christmas/index.html", {
        "christmas": now.month == 1 and now.day == 1                                                
    })
