import socket
import RPi.GPIO as GPIO          
from time import sleep
'''elif dc1 > 0 and dc2 <= 0:
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)
        
       elif dc1 <= 0 and dc2 > 0:
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)'''
def sigmoid(x):
        return (1/(1+2.71828**(x)) - 0.5) * 2

def epicness(pitch, yaw):
        if yaw > 1:
                #turns left at max speed
                dc1 = 100
                dc2 = 100
               
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)
        if yaw < 0:
                #turns right at max speed
                print("R")
                dc1 = 100
                dc2 = 100
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)    
        pitch = -pitch
        yaw = -yaw
        max = 100
        k = 45
        dc1 = max*sigmoid(pitch/k)
        diff = 2 * max * sigmoid(yaw/k)
        print(diff)
        dc2 = dc1 - diff
        print([dc1, dc2])
        
        if dc1 > max:
                dc1 = max
        elif dc1 < -max:
                dc1 = -max
        if dc2 > max:
                dc2 = max
        elif dc2 < -max:
                dc2 = -max
        
        if dc1 > 0 and dc2 > 0:
                #Forward

                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)
    
        elif dc1 < 1 and dc2 < 1:
                #Backward
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)
                
        p1.ChangeDutyCycle(int(abs(dc1)))
        p.ChangeDutyCycle(int(abs(dc2)))
        
        if abs(dc1) <= 10:
            dc1 = 0
        if abs(dc2) <= 10:
            dc2 = 0
            
        if abs(dc1 - dc2) <= 10:
            avg = (dc1 + dc2)/2
            dc1 = avg
            dc2 = avg
        
        print([dc1, dc2])

in3 = 24
in4 = 21
in1 = 7
in2 = 8
en = 25
enb = 9
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(en,1000)
p1 = GPIO.PWM(enb, 1000)
p.start(25)
p1.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 5000  # Choose the same port number as in the Android code

def handle_client_connection(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break

        # Process the received data
        received_data = data.decode('utf-8')
        stuff = received_data.split(": ")
        print(' ')
        x = 0
        for i in range(len(stuff)):
            if 'Z' in list(stuff[i]):
                try:
                    pitch = float(stuff[i][0:-2])
                    x += 1
                except:
                    x = x
        try:
            yaw = float(stuff[-1])
            x += 1
        except:
            x = x
            
        
        
        if x == 2:
            epicness(pitch, yaw)
            sleep(.01)
            
        print(' ')
        print(' ')

        # Add your logic here to handle the received gyrodata

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Set the option to reuse the socket address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to a specific host and port
    server_socket.bind((HOST, PORT))
    # Listen for incoming connections
    server_socket.listen(1)
    print('Waiting for a connection...')

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print('Connected to:', client_address)

        # Handle the client connection in a separate thread
        handle_client_connection(client_socket)
