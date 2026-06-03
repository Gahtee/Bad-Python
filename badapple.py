import cv2
import os
import time

video = cv2.VideoCapture("badapple.mp4")

fps = video.get(cv2.CAP_PROP_FPS)
delay = 1 / fps
LARGURA = 63
input()
while True:
    ret, frame = video.read()

    if not ret:
        break

    altura_original, largura_original = frame.shape[:2]

    altura = int((altura_original / largura_original) * LARGURA * 0.5)

    frame = cv2.resize(frame, (LARGURA, altura))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    texto = []

    for y in range(altura):
        linha = ""

        for x in range(LARGURA):
            if gray[y, x] > 127:
                linha += "⬜"
            else:
                linha += "⬛"

        texto.append(linha)

    os.system("cls")  # Windows

    print("\n".join(texto))

    time.sleep(delay-0.009999999999999)

video.release()