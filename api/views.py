import requests
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.urls import reverse

def index(request):
    """
    Renders the index page that provides an overview of the project
    and how to use the API to access package information.
    """
    return render(request, 'api/index.html')

def get_json(request, name):
    """
    Fetches package information from PyPI and returns rendered HTML 
    in JSON format.
    """
    default_data = {
        "name": "Package Not Found",
        "version": "",
        "summary": f"The package '{name}' is not a valid PyPi package.",
        "author": "sorry!",
        "release_url": reverse('index'),
    }
    
    url = f'https://pypi.org/pypi/{name}/json'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as _e:
        # Handle request errors, return 404 status
        formatted_html = render_to_string('api/card.html', {'info': default_data})
        return JsonResponse({'html': formatted_html}, status=404)

    data = response.json()
    formatted_html = render_to_string('api/card.html', {'info': data['info']})
    return JsonResponse({'html': formatted_html}, status=200)

def get_html(request, name):
    """
    Fetches package information from PyPI and returns the rendered HTML page.
    """
    default_data = {
        "name": "Package Not Found",
        "version": "",
        "summary": f"The package '{name}' is not a valid PyPi package.",
        "author": "sorry!",
        "release_url": reverse('index'),
    }
    
    url = f'https://pypi.org/pypi/{name}/json'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException:
        return render(request, 'api/card.html', {'info': default_data}, status=404)

    data = response.json()
    return render(request, 'api/card.html', {'info': data['info']})
