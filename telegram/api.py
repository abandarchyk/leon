import httptransport

http_endpoint = httptransport.Endpoint()


def get_updates():
    print('Telegram API: getUpdates is calling')
    http_response = http_endpoint.http_get('getUpdates')
    # extract updates
    # return updates

def send_message(message):
    http_endpoint.http_post('sendMessage', message)
