from time import sleep
import cv2
import paho.mqtt.client as paho
import sys

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect!")
    sys.exit(-1)

A_hand = cv2.CascadeClassifier('haar/A.xml')
B_hand = cv2.CascadeClassifier('haar/B-1.1-10.xml')
C_hand = cv2.CascadeClassifier('haar/C-2-10.xml')
D_hand = cv2.CascadeClassifier('haar/D-2-10.xml')
E_hand = cv2.CascadeClassifier('haar/E.xml')
F_hand = cv2.CascadeClassifier('haar/F.xml')
G_hand = cv2.CascadeClassifier('haar/G.xml')
H_hand = cv2.CascadeClassifier('haar/H.xml')
I_hand = cv2.CascadeClassifier('haar/I.xml')
K_hand = cv2.CascadeClassifier('haar/K.xml')
L_hand = cv2.CascadeClassifier('haar/L.xml')
J_hand = cv2.CascadeClassifier('haar/J.xml')
M_hand = cv2.CascadeClassifier('haar/M.xml')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.rectangle(frame, (100, 100), (350, 350), (0, 255, 0), 3)
    crop = frame[100:350, 100:350]
    frame = cv2.flip(frame, 1)
    crop_img = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

    A = A_hand.detectMultiScale(crop_img, 2, 10)
    B = B_hand.detectMultiScale(crop_img, 1.5, 10)
    C = C_hand.detectMultiScale(crop_img, 2, 10)
    D = D_hand.detectMultiScale(crop_img, 1.1, 10)
    E = E_hand.detectMultiScale(crop_img, 1.5, 10)
    F = F_hand.detectMultiScale(crop_img, 1.5, 10)
    G = G_hand.detectMultiScale(crop_img, 1.5, 10)
    H = H_hand.detectMultiScale(crop_img, 1.5, 10)
    I = I_hand.detectMultiScale(crop_img, 1.1, 10)
    K = K_hand.detectMultiScale(crop_img, 2, 10)
    L = L_hand.detectMultiScale(crop_img, 1.5, 10)
    J = J_hand.detectMultiScale(crop_img, 1.1, 10)
    M = M_hand.detectMultiScale(crop_img, 1.1, 10)

    for (hx, hy, hw, hh) in A:
        cv2.putText(frame, 'A', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "A", 0)
    for (hx, hy, hw, hh) in B:
        cv2.putText(frame, 'B', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "B", 0)
    for (hx, hy, hw, hh) in C:
        cv2.putText(frame, 'C', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "C", 0)
    for (hx, hy, hw, hh) in D:
        cv2.putText(frame, 'D', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "D", 0)
    for (hx, hy, hw, hh) in E:
        cv2.putText(frame, 'E', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "E", 0)
    for (hx, hy, hw, hh) in F:
        cv2.putText(frame, 'F', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "F", 0)
    for (hx, hy, hw, hh) in G:
        cv2.putText(frame, 'G', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "G", 0)
    for (hx, hy, hw, hh) in H:
        cv2.putText(frame, 'H', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "H", 0)
    for (hx, hy, hw, hh) in I:
        cv2.putText(frame, 'I', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "I", 0)
    for (hx, hy, hw, hh) in K:
        cv2.putText(frame, 'K', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "K", 0)
    for (hx, hy, hw, hh) in L:
        cv2.putText(frame, 'L', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "L", 0)
    for (hx, hy, hw, hh) in J:
        cv2.putText(frame, 'J', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "J", 0)
    for (hx, hy, hw, hh) in M:
        cv2.putText(frame, 'M', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)
        client.publish("testing", "M", 0)

    cv2.imshow('cropped', crop_img)
    cv2.imshow('Main', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
