import paho.mqtt.client as mqtt
import login_data
import sander

def on_message(client, usrdata,  msg):
    msg_from_client = str(msg.payload.decode())
    print('[info] ', 'received: ', msg_from_client)
    sander.sand_to_client(msg_from_client)

def iniz():
    global client
    client = mqtt.Client()
    client.username_pw_set(login_data.get_server_data('login'), login_data.get_server_data('pwd'))
    client.on_message = on_message
    client.connect(login_data.get_server_data('server_ip'), int(login_data.get_server_data('server_port')), keepalive=0)

def start_listener():
    global client
    client.subscribe(login_data.get_server_data('cmd_room'))
    client.loop_forever()


