def handler(request):
    query = request.args
    mode = query.get('hub.mode')
    token = query.get('hub.verify_token')
    challenge = query.get('hub.challenge')

    if mode == 'subscribe' and token == 'innerg-secret':
        return challenge or '', 200
    else:
        return 'Forbidden', 403
