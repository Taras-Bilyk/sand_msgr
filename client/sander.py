#import paho.mqtt.client as mqtt
import login_data
#import receiver
import receiver
#client = mqtt.Client()
#client.username_pw_set(login_data.get_data('login'), login_data.get_data('pwd'))
#client.connect(login_data.get_data('server_ip'), int(login_data.get_data('server_port')), keepalive=0)

def sand_to_server(username, room, data):
    client = receiver.client
    data_to_publish = {'username' : username, 'room' : room, 'data' : data}
    client.publish(login_data.get_data('cmd_room'), str(data_to_publish))





