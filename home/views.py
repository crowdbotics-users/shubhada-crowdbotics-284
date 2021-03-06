from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'django-trackstats', 'url': 'http://pypi.python.org/pypi/django-trackstats/0.5.0'},
	{'name':'django-trackstats', 'url': 'http://pypi.python.org/pypi/django-trackstats/0.5.0'},
	{'name':'django-request', 'url': 'http://pypi.python.org/pypi/django-request/1.5.4'},
	{'name':'django-experiments', 'url': 'http://pypi.python.org/pypi/django-experiments/1.2.0'},
	{'name':'django-app-metrics', 'url': 'http://pypi.python.org/pypi/django-app-metrics/0.9.0'},
	{'name':'django-analytical', 'url': 'http://pypi.python.org/pypi/django-analytical/2.4.0'},
	{'name':'satchless', 'url': 'http://pypi.python.org/pypi/satchless/1.1.3'},
	{'name':'satchless', 'url': 'http://pypi.python.org/pypi/satchless/1.1.3'},
	{'name':'django-shop', 'url': 'http://pypi.python.org/pypi/django-shop/0.11.3'},
	{'name':'django-oscar', 'url': 'http://pypi.python.org/pypi/django-oscar/1.5.1'},
	{'name':'spirit', 'url': 'http://pypi.python.org/pypi/spirit/1.7.0'},
	{'name':'spirit', 'url': 'http://pypi.python.org/pypi/spirit/1.7.0'},
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
