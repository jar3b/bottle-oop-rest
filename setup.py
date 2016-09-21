from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='bottle-oop-rest',
    version='0.0.1',
    packages=['borest'],
    url='https://github.com/jar3b/bottle-oop-rest',
    license='MIT',
    author='hello',
    author_email='hellotan@live.ru',
    description='Bottle.py OOP REST simple library',
    install_requires=required
)
