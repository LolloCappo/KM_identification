with open('README.rst', 'r') as f:
    readme = f.read()
    
from setuptools import setup, Extension
from ThermCoeff import __version__

if __name__ == '__main__':
    setup(name='ThermCoeff',
        version=__version__,
        author='Lorenzo Capponi',
        author_email='lorenzocapponi@outlook.it',
        description='Module for thermoelastic coefficient identification',
        url='https://github.com/LolloCappo/ThermCoeff',
        py_modules=['ThermCoeff'],
        long_description=readme,
        install_requires = ['numpy>=1.16.5','pyLIA>=0.6']

      )
