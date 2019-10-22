from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Register your models here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(["POST"])
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.succss(request, f'Account created for {username}!')
            return JsonResponse({'response':'success'})
    else:
        form = userCreationForm()

    return JsonResponse({'response':'not success'})