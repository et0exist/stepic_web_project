def wsgi_application(environ, start_response):
    from cgi import parse_qs

    params = parse_qs(environ['QUERY_STRING'])
    body_str = ''
    for i in params:
        body_str += params[i][0] + '\n'
    body_str = body_str.strip()
    
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
    ]
    body = [body_str]
    start_response(status, headers)
    return [body]
