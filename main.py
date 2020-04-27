from machine import Pin, SPI
import config as cfg
from vectors import vectors
import time



def configure_spi():
    """
    Configure SPI
    """
    hspi = SPI(1, baudrate=cfg.BAUDRATE, polarity=cfg.POLARITY, phase=cfg.PHASE)

    return hspi

def run_vectors(spi):
    """
    Writes all vectors over SPI
    """

    csb = Pin(15, Pin.OUT)
    csb.on()

    csb.off()
    for vector in vectors:
        print(bytes(vector))
        spi.write(bytes(vector))

    csb.on()

    return

def check_vectors():
    """
    Read Back vectors to check they were written correctly
    """

def confirm_ok(visual=True):
    """
    Confirm vectors correct using LED pulse and status flag on pin
    """

    if visual:

        led = Pin(16, Pin.OUT)
        #time.sleep(0.2)
        led.off()
        time.sleep(0.1)
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.1)
        led.on()

def run():
    time.sleep(0.8)
    Pin(15, Pin.OUT).on()


    spi = configure_spi()
    run_vectors(spi)
    confirm_ok()


run()