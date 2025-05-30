import time
import busio
import digitalio
import board
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn
from adafruit_mcp3xxx.mcp3008 import P0  # Channel 0 for LDR

# Setup SPI on Raspberry Pi
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D8)
mcp = MCP3008(spi, cs)

# Setup analog input channel 0 (LDR voltage divider)
chan = AnalogIn(mcp, P0)

# Max voltage (Vcc)
VCC = 3.3

# Function to classify jaundice based on voltage (0V to 3.3V)
def classify_jaundice_voltage(voltage):
    # Set your voltage thresholds here (adjust after calibration)
    if voltage > 2.7:
        return "Severe Jaundice"
    elif voltage > 2.0:
        return "Moderate Jaundice"
    elif voltage > 1.3:
        return "Mild Jaundice"
    else:
        return "Normal"

print("Starting jaundice detection (voltage based)...\n")

try:
    while True:
        voltage = chan.voltage  # Read voltage from MCP3008
        status = classify_jaundice_voltage(voltage)
        print(f"Voltage: {voltage:.2f} V | Status: {status}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")
