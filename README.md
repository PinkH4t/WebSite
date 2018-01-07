# What

The sources of the website at http://pinkh4t.com

# How

## Overview

- `config.yml` : the main configuration file.
- `web/run.py` : the front controller, holding most of the code.
- `web/templates/home.html.jinja2` : the HTML template.


## Install

``` bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Develop

``` bash
source venv/bin/activate
python web/run.py
```

Then, browse [localhost:5000](http://localhost:5000).