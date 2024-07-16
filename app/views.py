from django.shortcuts import render

# Create your views here.
def index(request):
    car_list = [
        {'brand': 'Toyota'},
        {'brand': 'Nissan'},
        {'brand': 'Honda'},
    ]
    context = {
        'car_list': car_list
    }
    return render(request, 'app/index.html', context)
