from time import sleep
import cv2
import paho.mqtt.client as paho
import sys

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect!")
    sys.exit(-1)

B_hand = cv2.CascadeClassifier('haar/B-1.1-10.xml')
C_hand = cv2.CascadeClassifier('haar/C-2-10.xml')
D_hand = cv2.CascadeClassifier('haar/D-2-10.xml')
E_hand = cv2.CascadeClassifier('haar/E.xml')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.rectangle(frame, (100, 100), (350, 350), (0, 255, 0), 3)
    crop = frame[100:350, 100:350]
    crop_img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

    B = B_hand.detectMultiScale(crop_img, 1.1, 10)
    C = C_hand.detectMultiScale(crop_img, 2, 10)
    D = D_hand.detectMultiScale(crop_img, 1.5, 10)
    E = E_hand.detectMultiScale(crop_img, 1.1, 10)

    for (hx, hy, hw, hh) in B:
        cv2.putText(frame, 'B', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "A", 0)
    for (hx, hy, hw, hh) in C:
        cv2.putText(frame, 'C', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "C", 0)
    for (hx, hy, hw, hh) in D:
        cv2.putText(frame, 'D', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "D", 0)
    for (hx, hy, hw, hh) in E:
        cv2.putText(frame, 'E', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "E", 0)

    cv2.imshow('cropped', crop_img)
    cv2.imshow('Main', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
