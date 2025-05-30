import busio
import digitalio
import board
from adafruit_mcp3xxx.mcp3008 import MCP3008
from adafruit_mcp3xxx.analog_in import AnalogIn
from adafruit_mcp3xxx.mcp3008 import P0

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D8)
mcp = MCP3008(spi, cs)
chan = AnalogIn(mcp, P0)

def read_voltage():
    return chan.voltage
