# bottle-oop-rest
Bottle.py OOP REST simple library, supports "OPTIONS" out of the box

## Example usage
```
from borest import app, Route

@Route('/hello/<username>')
class Hello:
    msg = "HELLO, "

    def get(self, username=None):
        return self.msg + username

    def post(self, username=None):
        return "Don't post me, " + username


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
```

Error handling (now handler must be a function, not class):
```
@Error(404)
def error_404(error_msg):
    return "404: Page not found"

@Error([404, 500])
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
Content-Length: 0
Access-Control-Allow-Origin: *
```

## Changelog
- 0.0.4
    - Added "Access-Control-Allow-Headers" header into "OPTIONS" handler
    - Fix multiple error handling
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