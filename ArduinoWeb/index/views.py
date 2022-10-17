from django.shortcuts import render, redirect
from index.controller import *
from index.models import *
import schedule

# Create your views here.
def index_view (request):
    if request.POST:
        id = request.POST['id']
        if int(id) == 1:
            print("Allumons la LED Bleue")
            redOn()
        elif int(id) == 2:
            print("Allumons la LED Rouge")
            greenOn()
        elif int(id) == 3:
            print("Allumons la LED Verte")
            blueOn()
        elif int(id) == 4:
            print("Allumons la LED Jaune")
            yellowOn()
        elif int(id) == 5:
            allOff()
            print("Eteignons toutes les LED")
        elif int(id) == 6:
            blinkall()
        elif int(id) == 7:
            fonction()
        # print(id)
    # ,{'valeur_lue' : valeur}
    valeur = AHT20.objects.all()
    valeur = reversed(valeur)
    return render(request, 'index.html',{'valeur_lue' : valeur})