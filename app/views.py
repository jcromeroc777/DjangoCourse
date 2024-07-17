from django.shortcuts import render
from django.views.generic import TemplateView

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

class CarView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self):
        car_list = [
            {'brand': 'Toyota'},
            {'brand': 'Nissan'},
            {'brand': 'Honda'},
        ]
        return {
            'car_list': car_list
        }