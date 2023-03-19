from django.shortcuts import render
from num2words import num2words


def index(request):
    if request.method == 'POST':
        number = request.POST['number']
        try:
            number = int(number)
            if number < 0:
                message = 'Number must be positive'
            else:
                message = num2words(number)
        except ValueError:
            message = 'Please enter a valid number'
    else:
        message = ''
    return render(request, 'index.html', {'message': message})




