import thread
import time
import random

def tick_variavel(delay, variavel):
    while True:
        time.sleep(delay)
        variavel += random.uniform(-0.2, 0.2)
        if variavel > 5:
            variavel = 5
        if variavel < 0:
            variavel = 0
