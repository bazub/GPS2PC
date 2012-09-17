'''
Created on Sep 11, 2012

@author: Bogdan
'''
'''
a=input()
print (a)




HOLUX GPSlim236
00:0B:0D:85:24:53
'''
# coding: utf-8
import time
import webbrowser
import serial
ser = serial.Serial(
    port='COM3',
    baudrate=38400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.close()
print(ser.isOpen())

ser.open()
print(ser.isOpen())
while 1:
    a=ser.readline()
    pos=[]
    k=0
    STR=[]
    for i in range (0,len(a)):
        if a[i]==',':
            pos.append(i)
            k=k+1
    for i in range(1,k):
        STR.append(a[pos[i-1]+1:pos[i]])
    if(a[:pos[0]]=="$GPGGA"):
        print(str(int(STR[1][:-7]))+"d"+str(int(STR[1][-7:-5]))+"'"+str(float(STR[1][-4:])*6/1000)+'"'+STR[2])
        print(str(int(STR[3][:-7]))+"d"+str(int(STR[3][-7:-5]))+"'"+str(float(STR[3][-4:])*6/1000)+'"'+STR[4])
        tomap=str(int(STR[1][:-7]))+'+'+str(int(STR[1][-7:-5]))+'+'+str(float(STR[1][-4:])*6/1000)+STR[2]+'+'+str(int(STR[3][:-7]))+'+'+str(int(STR[3][-7:-5]))+'+'+str(float(STR[3][-4:])*6/1000)+STR[4]
        handle = webbrowser.get()
        handle.open_new_tab('http://maps.google.com/?q='+tomap)

        break