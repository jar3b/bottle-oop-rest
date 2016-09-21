# bottle-oop-rest
Bottle.py OOP REST simple library

## Example usage
```
from borest import BoRest

class App(BoRest):
    def __init__(self):
        super(App, self).__init__()

    @BoRest.view('/hello/<username>')
    class Hello:
        @staticmethod
        def get(username):
            return "HELLO "+username

        @staticmethod
        def post(username):
            return "You cannot POST hello "+username
```

## Publishing
```
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest
python setup.py register -r pypi
python setup.py sdist upload -r pypi