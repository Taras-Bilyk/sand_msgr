import paho.mqtt.client as mqtt
import login_data
import listener

#client = mqtt.Client()
#client.username_pw_set(login_data.get_server_data('login'), login_data.get_server_data('pwd'))
#client.connect(login_data.get_server_data('server_ip'), int(login_data.get_server_data('server_port')), keepalive=0)

def sand_to_client(data):
    decoded_data_array = eval(data)
    client_username = str(decoded_data_array['username'])
    client_room = login_data.get_server_data('root_room') + str(decoded_data_array['room'])
    client_msg = str(decoded_data_array['data'])

    msg_to_sand_to_client = client_username + ': ' + client_msg

    listener.client.publish(client_room, msg_to_sand_to_client)
    #print('yap')

