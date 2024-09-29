import requests
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render

def index(request):
    """
    Renders the index page that provides an overview of the project
    and how to use the API to access package information.
    """
    return render(request, 'api/index.html')

def get_json(request, name):
    url = f'https://pypi.org/pypi/{name}/json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        # Render the template as a string
        formatted_html = render_to_string('api/card.html', {'data': data})
        
        # Return the rendered HTML in the JSON response
        return JsonResponse({'html': formatted_html})
    else:
        return JsonResponse({'error': 'Package not found'}, status=404)

def get_html(request, name):
    url = f'https://pypi.org/pypi/{name}/json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return render(request, 'api/card.html', {'info': data['info']})
    else:
        return render(request, 'error.html', {'error': 'Package not found'}, status=404)

