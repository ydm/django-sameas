# SameAs #
Repeat template blocks with ease!

## What is it? ##
**SameAs** is a small Django application that provides you with an
easy-to-use template tag to replicate a block.

For example you may want to repeat your title block somewhere else in
your page.
```html
{% load sameastags %}
...
  <head>
    <title>{% block title %}{{ object.title }}{% endblock %}</title>
  </head>
  <body>
    <h1>{% sameas title %}</h1>
  </body>
...
```
It's as simple as this.

But the real benefit of this feature is when used with template
inheritance.
```html
base.html:
...
    <title>{% block title %}{% endblock %}</title>
    <meta property="og:title" content="{% sameas title %}">
...

inner.html
...
{% extends "base.html" %}
{% block title %}{{ object.title }}{% endblock %}
...
```

## Installation ##
The application is currently not available on PyPI.  To install it,
you need to
* Clone this repository
* Add **sameas** package to PYTHONPATH
* Add **'sameas'** to your INSTALLED_APPS

### Requirements ###
* Python 2 or 3
* Django (tested against 1.5, but I expect it to work with previous
  versions too)

## Tests ##
If you're interested in the project and you contribute, please make
sure:
* your changes don't break current tests
* you add appropriate tests for your features/bug fixes.

To run the tests simply use  
`$ ./manage.py test sameas`

## License ##
This project is licensed under LGPLv3.  Read LICENSE for details.

#### Why it's not on PyPI? ####
I don't want to flood PyPI with something as simple as 20 lines
of code.  If the project turns out to be of valuable help, I'll
reconsider.
