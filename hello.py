def wsgi_application(environ, start_response):
    from cgi import parse_qs

    params = parse_qs(environ['QUERY_STRING'])
    body = ''
    for i in params:
        body += params[i][0] + '\n'
    
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return [body]
