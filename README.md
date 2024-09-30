[![Django Tests](https://github.com/bboonstra/pipembeds/actions/workflows/django-tests.yml/badge.svg)](https://github.com/bboonstra/pipembeds/actions/workflows/django-tests.yml)

# PipEmbeds

PipEmbeds is a project that allows you to easily embed or retrieve information about Python packages hosted on PyPI. Whether you're looking to display package details on your website or access information programmatically, this API has you covered.

## API Endpoints

Display package information via our third-party API:

- **JSON Format**: `/json/<package_name>/`
- **HTML Format**: `/html/<package_name>/`

### Response Formats

- **JSON Response**: `/json/` returns a JSON object of the pip embed in the following format:
  ```json
  {
      "html": "<div class='card'>...</div>"
  }
  ```

- **HTML Response**: `/html/` returns a fully rendered HTML page of the pip embed. This can be embedded directly in an iframe.

## Customization Options

Enhance the appearance of the package cards using the following query parameters:

- **`theme`**: Set to `dark` or `light` for different color schemes.
- **`text_color`**: Specify a hex color for text (e.g., `#fff` for white).
- **`button_color`**: Specify a hex color for buttons (e.g., `#007bff` for blue).
- **`border_color`**: Specify a hex color for the card border (e.g., `#ddd` for light gray).
- **`background_color`**: Specify a hex color for the card background (e.g., `#fff` for white).

### Example Usage

To get started, replace `<package_name>` with the name of the package you want to view, and add any desired customization options. For example:

- JSON request with custom colors:
  ```
  https://pipembeds.onrender.com/json/<package_name>/?theme=dark&text_color=#fff&button_color=#007bff&border_color=#ddd&background_color=#333
  ```

- HTML request with default options:
  ```
  https://pipembeds.onrender.com/html/<package_name>/
  ```

## Getting Started

To use the API, simply replace `<package_name>` with the name of the package you want to view. You can test the API using any HTTP client, such as your web browser, Postman, or cURL.