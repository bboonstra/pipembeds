import requests
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.urls import reverse

def fetch_package_info(name):
    """
    Fetches package information from PyPI.
    Returns the package data if found; otherwise, returns a default data dictionary.
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
        return response.json().get('info', default_data)
    except requests.exceptions.RequestException:
        return default_data

def render_card_response(request, name):
    """
    Fetches package information and returns rendered HTML based on the request type.
    """
    package_info = fetch_package_info(name)
    theme = request.GET.get('theme', 'dark')  # Default theme to dark
    text_color = request.GET.get('text_color', '#000')  # Default text color
    button_color = request.GET.get('button_color', '#007bff')  # Default button color
    border_color = request.GET.get('border_color', '#ddd')  # Default border color
    background_color = request.GET.get('background_color', '#fff')  # Default background color

    # Prepare the context for rendering
    context = {
        'info': package_info,
        'theme': theme,
        'text_color': text_color,
        'button_color': button_color,
        'border_color': border_color,
        'background_color': background_color,
    }

    if request.content_type == 'application/json':
        # Render to string for JSON response
        formatted_html = render_to_string('api/card.html', context)
        return JsonResponse({'html': formatted_html}, status=200 if package_info['name'] != "Package Not Found" else 404)
    else:
        # Render the HTML page
        return render(request, 'api/card.html', context)

def index(request):
    """
    Renders the index page that provides an overview of the project
    and how to use the API to access package information.
    """
    return render(request, 'api/index.html')

def get_json(request, name):
    """
    Handles requests for JSON responses.
    """
    return render_card_response(request, name)

def get_html(request, name):
    """
    Handles requests for HTML responses.
    """
    return render_card_response(request, name)
