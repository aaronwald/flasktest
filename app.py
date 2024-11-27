from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Hello, World!</title>
      </head>
      <body>
        <div class="container">
          <h1>Hello, World!</h1>
          <p>This is a simple HTML page served by Flask.</p>
        </div>
      </body>
    </html>
    '''

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)