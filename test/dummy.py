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
