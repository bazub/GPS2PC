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
from Tkinter import *
import datetime
import os

def golog():
    os.system("notepad.exe "+"C:/Users/Bogdan/git/GPS2PC/GPS2PC/log.txt")

def gomaps():
    global tomap
    try:
        handle = webbrowser.get()
        handle.open_new_tab('http://maps.google.com/?q='+tomap)
    
    except NameError:
        pass
    
def getcoord():
    global x,y,var,lab,tomap,fout
    ser = serial.Serial(
        port='COM3',
        baudrate=38400,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    ser.close()
    ser.open()
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
            x=str(int(STR[1][:-7]))+"d "+str(int(STR[1][-7:-5]))+"' "+str(float(STR[1][-4:])*6/1000)+'" '+STR[2]
            y=str(int(STR[3][:-7]))+"d "+str(int(STR[3][-7:-5]))+"' "+str(float(STR[3][-4:])*6/1000)+'" '+STR[4]
            tomap=str(int(STR[1][:-7]))+'+'+str(int(STR[1][-7:-5]))+'+'+str(float(STR[1][-4:])*6/1000)+STR[2]+'+'+str(int(STR[3][:-7]))+'+'+str(int(STR[3][-7:-5]))+'+'+str(float(STR[3][-4:])*6/1000)+STR[4]
            var.set(x+'\n'+y)
            #lab.grid(row=1,rowspan=2, column=1,sticky=N+S+E)
            '''
            handle = webbrowser.get()
            handle.open_new_tab('http://maps.google.com/?q='+tomap)
            '''
            now=datetime.datetime.now()
            fout.write(now.strftime("%Y-%m-%d %H:%M:%S")+'\t'+'\t'+tomap+'\n')
            return (x,y)
            
    ser.close()
fout=open("log.txt","a")        
x=''
y=''        
root=Tk()
root.geometry("420x420+400+100")
root.title("GPS Thingy                          by Bazub")
root.bind("<Escape>", lambda e: e.widget.quit())
root.resizable(FALSE,FALSE)
photo=PhotoImage(file="worldlg.gif")
ca=Canvas(root)
ca.create_image(200,123,image=photo)
ca.grid(row=0,column=0,columnspan=2,sticky=N+S+E+W)
butGC=Button(root, text="Get coordinates", command=getcoord)
butGC.grid(row=1,column=0, sticky=N+S+E+W)
var=StringVar()
lab =Label(root, bg='white',width=50,height=2,textvariable=var,justify=CENTER)
lab.grid(row=1, column=1,sticky=N+S+E)
lab2=Label(root)
lab2.grid(row=2,column=0)
butG2S=Button(root, text="Go to Maps", command=gomaps)
butG2S.grid(row=3,column=0,columnspan=2, sticky=N+S+E+W)
lab3=Label(root)
lab3.grid(row=4,column=0)
butWHIB=Button(root,text="Where have I been?",command=golog)
butWHIB.grid(row=5,column=0,columnspan=2,sticky=N+S+E+W)

root.mainloop()

        