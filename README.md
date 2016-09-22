# bottle-oop-rest
Bottle.py OOP REST simple library

## Example usage
```
from borest import app, Route, Error
import json
from time import sleep


@Route('/hello/<username>')
class Hello:
    msg = "HELLO, "

    def get(self, username=None):
        return self.msg + username

    def post(self, username=None):
        return "Don't post me, " + username


@Route('/sleep/<cnt>')
class GeventAsync:
    def get(self, cnt):
        for x in range(0, int(cnt)):
            yield 'Iteration #%s' % x
            sleep(3)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, server='gevent')
```

Warning! For using gevent you must import `from borest ...` as first string in your app module

Error handling (now handler must be a function, not class and not class method):
```
@Error(404)
def error_404(error_msg):
    return "404: Page not found"

@Error([405, 500])
def errors(http_error):
    return json.dumps(dict(error=http_error.status))
```

Output for GET /hello/jack:
```
HELLO, jack
```

Output for POST /hello/jack:
```
Don't post me, jack
```

Headers for OPTIONS /hello/jack:
```
Access-Control-Allow-Methods: OPTIONS, GET, POST
Access-Control-Allow-Headers: x-requested-with, content-type, accept, origin, authorization, x-csrftoken, user-agent, accept-encoding
Content-Length: 0
Access-Control-Allow-Origin: *
```

## Changelog
- 0.0.4
    - Added "Access-Control-Allow-Headers" header into "OPTIONS" handler
    - Fix multiple error handling
    - Add gevent support (cannot be disabled)
- 0.0.3
    - Added simple error processing
- 0.0.2
    - Code refactoring
    

## Publishing
```
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest
python setup.py register -r pypi
python setup.py sdist upload -r pypi