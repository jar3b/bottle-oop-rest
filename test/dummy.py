from borest import app, Route, Error
import json
from time import sleep


@Route(['/hello/<username>', '/hello'])
class Hello:
    msg = "HELLO, "

    def get(self, username="Anonimous"):
        return self.msg + username

    def post(self, username="Anonimous"):
        return "Don't post me, " + username


@Route('/sleep/<cnt>')
class GeventAsync:
    def get(self, cnt):
        for x in range(0, int(cnt)):
            yield 'Iteration #%s' % x
            sleep(3)


@Error([404])
def errors(http_error):
    return json.dumps(dict(error=http_error.status))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, server='gevent')
