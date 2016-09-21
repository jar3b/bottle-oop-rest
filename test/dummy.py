import json

from borest import app, Route, Error


@Route('/hello/<username>')
class Hello:
    msg = "HELLO, "

    def get(self, username=None):
        return self.msg + username

    def post(self, username=None):
        return "Don't post me, " + username


@Error([404, 500])
def errors(http_error):
    return json.dumps(dict(error=http_error.status))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
