
# Main Code Contributions:
# SPDX-FileCopyrightText: 2021 Team 4160 "The Robucs" Mission Bay HighSchool
# SPDX-License-Identifier: MIT
# Some Code greatfully reused from:
# SPDX-FileCopyrightText: 2019 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
#==================================== 
import time
import board
import busio
from adafruit_seesaw.seesaw import Seesaw
print("Libraries loaded")

# setup variables for sampling
#====================================
sleep_timer = 2.0
deep_sleep = 90
retries = 4
samples = 3
# setup for soil sensor
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
ss = Seesaw(i2c, addr=0x36)

# Functions
#====================================

def avg_soil(sleep_timer, samples):
    print("Testing Soil.  Takes 6+ seconds (or sleep_timer x samples)")
    count = 0
    total = 0
    while count < samples:
        total = total + ss.moisture_read()
        time.sleep(sleep_timer)
        count += 1
    soil = total / samples
    return (round(soil, 1))

# Main
#====================================
while True:
    try:
        print("Moisture:{}".format(avg_soil(sleep_timer, samples)))

    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
    time.sleep(deep_sleep)
