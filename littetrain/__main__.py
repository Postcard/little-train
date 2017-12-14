
from pifacedigitalio import PiFaceDigital
import config
import time


if __name__ == "__main__":

    pifacedigital = PiFaceDigital()
    input = pifacedigital.input_pins[config.INPUT_PIN]
    output = pifacedigital.relays[config.OUTPUT_PIN]

    while True:

        if input.value:
            output.turn_on()
            time.sleep(config.TIMER)
            output.turn_off()
        time.sleep(config.BOUNCE_TIME)


