import sys
if(sys.platform == 'esp8266'):
    import network
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    sta_if.connect('<Netw>', '<passw>')
    while not sta_if.isconnected():
        pass
    ap_if.active(False)
    print('Network Connected')


import socket 

recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind(('0.0.0.0', 8266))
recv_sock.settimeout(2)

send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if(sys.platform == 'linux'):
    send_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    send_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) 
print('Socket bind ok')


import time
while(True):
    try:
        recv_msg = recv_sock.recvfrom(1024)
        if(recv_msg):
            print(recv_msg)
    except:
        pass
    time.sleep(1)
    send_sock.sendto('aws', ('255.255.255.255', 8266))
