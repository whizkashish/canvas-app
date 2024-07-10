from django.shortcuts import render
from core.models import Stand

# Create your views here.
def Home(request):
    stands = Stand.objects.all()
    return render(request,"pages/index.html",{'stands':stands})