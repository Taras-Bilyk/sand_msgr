import paho.mqtt.client as mqtt
import shared_queue
import login_data

client = None


def on_message_from_server(client, usrdata, msg):
    msg_from_server = str(msg.payload.decode())
    shared_queue.queue.put(msg_from_server)

def initialize():
    global client
    client = mqtt.Client()
    #client.ws_set_options(path="/")
    client.username_pw_set(login_data.get_data('login'), login_data.get_data('pwd'))
    client.connect(login_data.get_data('server_ip'), int(login_data.get_data('server_port')), keepalive=0)

    client.on_message = on_message_from_server





room_name = None

def start_listening_server():
    global room_name, client
    room_name_to_subscribe = str(login_data.get_data('root_room')) + str(room_name)
    client.subscribe(room_name_to_subscribe)
    client.loop_forever()



