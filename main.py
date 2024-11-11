import RPi.GPIO as gpio
import time


def main():
    n = 2
    gpio.setmode(gpio.BCM)
    gpio.setup(n, gpio.OUT, initial=gpio.LOW)
    while True:
        gpio.output(n, gpio.HIGH)
        time.sleep(1)
        gpio.output(n, gpio.LOW)
        time.sleep(1)



if __name__ == '__main__':
    main()

