from wsgiref.simple_server import make_server

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style environment variables and the
# second variable is the callable object (see PEP 333).
def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    return [b"""<!DOCTYPE html>
    <html>
    <head>
    <title>My Python Web Server Test</title>
    </head>
    <body>
    <h1>If you can see this website, the server is working</h1>
    <p>Please remain for as long as needed</p>
    <p></p>
    <a href="https://www.google.com/" >Click here to go back to google</a>
    </body>
    </html>"""]

with make_server('', 8000, hello_world_app) as httpd:
    print("Serving on port 8000...")

    # Serve until process is killed
    httpd.serve_forever()