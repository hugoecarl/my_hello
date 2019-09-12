
from setuptools import setup 

setup(name='my_hello_hugoec', 
    version='0.2',
    packages=['my_hello'],
    author="HugoCarl",
    author_email="mormeme@gmail.com",
    description="Distribuição de software",
    install_requires=['numpy'],
    scripts=['scripts/hello.py']
    )