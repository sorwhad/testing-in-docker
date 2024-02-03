from flask import Flask

app = Flask('app')

@app.route('/')
def test():
    return '/'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8890)
