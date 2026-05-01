list_with_server_data = {
    'server_ip' : '127.0.0.1',
    'server_port' : '1883',
    'login' : 'guest',
    'pwd' : '12345',
    'cmd_room' : 'chat/w131313_zumi_zumi_zumi_zumi_zumi_zumi',
    'root_room' : 'sander_app_chat_zumi_zumi_zumi_zumi_zumi_zumi/'
}


def get_server_data(key):
    server_data_to_return = str(list_with_server_data[str(key)])
    return server_data_to_return



