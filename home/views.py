from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'Misago', 'url': 'http://pypi.python.org/pypi/Misago/0.14.0'},
	{'name':'Misago', 'url': 'http://pypi.python.org/pypi/Misago/0.14.0'},
	{'name':'djoser', 'url': 'http://pypi.python.org/pypi/djoser/1.1.5'},
	{'name':'djoser', 'url': 'http://pypi.python.org/pypi/djoser/1.1.5'},
	{'name':'django-stronghold', 'url': 'http://pypi.python.org/pypi/django-stronghold/0.3.0'},
	{'name':'django-stronghold', 'url': 'http://pypi.python.org/pypi/django-stronghold/0.3.0'},
	{'name':'django-social-auth', 'url': 'http://pypi.python.org/pypi/django-social-auth/0.7.28'},
	{'name':'django-social-auth', 'url': 'http://pypi.python.org/pypi/django-social-auth/0.7.28'},
	{'name':'django-guardian', 'url': 'http://pypi.python.org/pypi/django-guardian/1.4.9'},
	{'name':'django-guardian', 'url': 'http://pypi.python.org/pypi/django-guardian/1.4.9'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
