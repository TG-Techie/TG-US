from adafruit import adafruit_mcp9808

from tg_io.staging.pin_port import i2c_port

# This example shows how to get the temperature from a MCP9808 board
mcp = adafruit_mcp9808.MCP9808(i2c_port)

'''while True:
    tempC = mcp.temperature
    tempF = tempC * 9 / 5 + 32
    print('Temperature: {} C {} F '.format(tempC, tempF))
    time.sleep(2)'''