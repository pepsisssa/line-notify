import requests

def main():
    send_message_line_notify('新しいコード 312395773002。')

def send_message_line_notify(message):
    line_notify_token = 'lhJWSltbTmeL0vHJX2vJQq9ZZzAzaEMcRzHLi4yOeKC'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    data = {'message': message}
    requests.post(line_notify_api, headers=headers, data=data)

if __name__ == "__main__":
    main()


