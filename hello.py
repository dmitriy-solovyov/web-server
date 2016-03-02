from cgi import parse_qs, escape

def hello_world(environ, start_response):
    d = environ['QUERY_STRING']
    list = d.replace("&","\n")
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return list
