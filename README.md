# PipEmbeds
This project allows you to easily embed or get information about Python packages hosted on PyPI.

You can display package information via our third-party API:

JSON Format: /json/<package_name>/
HTML Format: /html/<package_name>/
/json/ returns a JSON object of the pip embed, with the format {'html': ""}.

/html/ returns an HTML page of the pip embed.

To get started, simply replace <package_name> with the name of the package you want to view.