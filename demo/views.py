from django.shortcuts import render
from demo.forms import DemoForm
from demo.models import DemoModel


def index(request):
    form = DemoForm()
    return render(request, 'index.html', {'form': form})


def add(request):
    form = DemoForm(request.POST)
    if form.is_valid():
        form.save()
        print("Form is valid")
    else:
        print("Form is not valid")

    data = DemoModel.objects.all()

    return render(request, 'all.html', {'data': data})
