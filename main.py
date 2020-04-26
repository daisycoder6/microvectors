from machine import Pin, SPI
import config as cfg
from vectors import vectors



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
    for vector in vectors:
        print(vector)
        #spi.write(vector)

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

        led = machine.Pin(2, machine.Pin.OUT)
        time.sleep(0.8)
        led.off()
        time.sleep(0.8)
        led.on()
        time.sleep(0.8)
        led.off()
        time.sleep(0.8)
        led.on()

def run():
    spi =configure_spi()
    run_vectors(spi)
    confirm_ok()


run()