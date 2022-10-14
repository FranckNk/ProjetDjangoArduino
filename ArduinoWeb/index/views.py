from django.shortcuts import render, redirect
from index.controller import *

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
        print(id)
    return render(request, 'index.html')