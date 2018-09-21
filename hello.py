def wsgi_application(environ, start_response):

    body = [bytes(i + '\n', encoding='utf-8') for i in environ['QUERY_STRING'].split(sep='&')]

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return iter(body)
