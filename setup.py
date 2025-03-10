from setuptools import setup

setup(
    name='httpie-image',
    description='Image display plugin for HTTPie.',
    version='1.0.0',
    author='banteg',
    url='https://github.com/banteg/httpie-image',
    py_modules=['httpie_image'],
    install_requires=['httpie', 'pillow', 'term-image'],
    entry_points={
        'httpie.plugins.converter.v1': [
            'httpie_image = httpie_image:ImagePlugin',
        ]
    },
)
