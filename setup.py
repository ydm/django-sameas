from distutils.core import setup

setup(
    name='django-sameas',
    version='0.1.0',
    author='Yordan Miladinov',
    author_email='jordanMiladinov@gmail.com',
    packages=['sameas','sameas.templatetags'],
    package_data={'sameas':['templates/*/*/*.html']},
    url='https://github.com/ydm/django-sameas',
    download_url='https://github.com/ydm/django-sameas/archive/0.1.0.tar.gz',
    license='LICENSE',
    description='Django application that provides you with an easy-to-use template tag that replicates a block.',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.4"
    ],
    keywords=['django', 'template tag', 'block'],
)
