import httptransport
import utils

print('pizdec')
props = utils.SystemProperties()
http_endpoint = httptransport.Endpoint(props.id)


def get_updates():
    print('Telegram API: getUpdates is calling')
    http_response = http_endpoint.http_get('getUpdates')
    print('Response:\n' + http_response.text)
    # extract updates
    # return updates

def send_message(message):
    http_endpoint.http_post('sendMessage', message)
