def application(env, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	for key in d:
    		start_response('200 OK', [('Content-Type','text/plain')])
    		return [key] # python3
