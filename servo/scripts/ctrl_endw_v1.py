#!/usr/bin/env python

# este programa envia una posiciona al motor del canal cero de pololu
import rospy  #importar rospy
from std_msgs.msg import Int16 
import numpy as np
import time
 
 
 
 

def callback_function_1(data): #funcion a la que se llama cuando recibo un mensaje en el topic al que nos subscribimos
   # rospy.loginfo("He recibido: %s y %f", data.stamp, data.num) #escribe en el log el mensaje recibido
   a=1


def callback_function_2(data): #funcion a la que se llama cuando recibo un mensaje en el topic al que nos subscribimos
   # rospy.loginfo("He recibido: %s y %f", data.stamp, data.num) #escribe en el log el mensaje recibido
      a=1
 
def callback_function_3(data): #funcion a la que se llama cuando recibo un mensaje en el topic al que nos subscribimos
  #  rospy.loginfo("He recibido: %s y %f", data.stamp, data.num) #escribe en el log el mensaje recibido
     a=1
def callback_function_4(data): #funcion a la que se llama cuando recibo un mensaje en el topic al que nos subscribimos
   # rospy.loginfo("He recibido: %s y %f", data.stamp, data.num) #escribe en el log el mensaje recibido
     a=1
 
#funcion principal
def principal():
    roll = rospy.Publisher('/EndoWrist/servo1/target', Int16, queue_size=10) #crea el publicador en el topic hola_mundo y tipo de mensaje int16
    
    yaw = rospy.Publisher('/EndoWrist/servo4/target', Int16, queue_size=10)
    pitch_1 = rospy.Publisher('/EndoWrist/servo2/target', Int16, queue_size=10)
    pitch_2 = rospy.Publisher('/EndoWrist/servo3/target', Int16, queue_size=10)
  
    # subscriptores
    rospy.Subscriber("/EndoWrist/servoOne/pos", Int16, callback_function_1)
    rospy.Subscriber("/EndoWrist/servoTwo/pos", Int16, callback_function_2)
    rospy.Subscriber("/EndoWrist/servoThree/pos", Int16, callback_function_3)
    rospy.Subscriber("/EndoWrist/servoFour/pos", Int16, callback_function_4)

  
    rospy.init_node('publicador', anonymous=True) #inicia el nodo publicador
    rate = rospy.Rate(0.5) # 0.5 Hz
    
    rospy.loginfo("Estoy publicando en el topic hola_mundo") #escribo en log
    while not rospy.is_shutdown(): #mientras ROS siga funcionando

        rospy.loginfo("motor roll") #escribo en log

        tt=2
        lstr = 1500
        a = np.int16(lstr)
        roll.publish(a)
        time.sleep(tt)

        lstr = 900
        a = np.int16(lstr)
        roll.publish(a)
        time.sleep(tt)


        # rospy.loginfo("motor yaw") #escribo en log



        # lstr = 1200
        # a = np.int16(lstr)
        # yaw.publish(a)
        # time.sleep(tt)

        # lstr = 900
        # a = np.int16(lstr)
        # yaw.publish(a)
        # time.sleep(tt)



        # rospy.loginfo("motor pitch_1") #escribo en log



        # lstr = 1200
        # a = np.int16(lstr)
        # pitch_1.publish(a)
        # time.sleep(tt)

        # lstr = 900
        # a = np.int16(lstr)
        # pitch_1.publish(a)
        # time.sleep(tt)



        # rospy.loginfo("motor pitch_2") #escribo en log



        # lstr = 1100
        # a = np.int16(lstr)
        # pitch_2.publish(a)
        # time.sleep(5)

        # lstr = 900
        # a = np.int16(lstr)
        # pitch_2.publish(a)
        # time.sleep(5)


        rospy.loginfo("abriendo pinza") #escribo en log



        lstr = 1100
        a = np.int16(lstr)
        pitch_1.publish(a)


        lstr = 1750
        a = np.int16(lstr)
        pitch_2.publish(a)
        time.sleep(5)


        rospy.loginfo("cerrando pinza") #escribo en log



        lstr = 1500
        a = np.int16(lstr)
        pitch_1.publish(a)


        lstr = 1400
        a = np.int16(lstr)
        pitch_2.publish(a)
        time.sleep(5)







        rate.sleep() 



    
    rospy.loginfo("Finalizando nodo...") #Si se para el nodo, escribe en el log
if __name__ == '__main__':
    try:
        principal()
    except rospy.ROSInterruptException:
        pass
