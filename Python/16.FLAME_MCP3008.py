# sudo apt-get install build-essential python3-dev python3-smbus python3-pip && sudo pip3 install adafruit-mcp3008

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time

# MCP3008 - 1 : 5V
# MCP3008 - 2 : 5V
# MCP3008 - 3 : GND
SCLK = 11   # MCP3008 - 4
MISO = 9    # MCP3008 - 5
MOSI = 10   # MCP3008 - 6
CE0 = 8     # MCP3008 - 7
# MCP3008 - 8 : GND
mcp = Adafruit_MCP3008.MCP3008(clk=SCLK, cs=CE0, miso=MISO, mosi=MOSI)

if __name__ == "__main__" :
    while(True) :
        #시간 설정
        now = time.localtime()
        timestamp = ("%04d-%02d-%02d %02d:%02d:%02d" % 
        (now.tm_year, now.tm_mon, now.tm_mday, 
        now.tm_hour, now.tm_min, now.tm_sec))

        values = [0]*8
        for i in range(8) :
            values[i] = mcp.read_adc(i)

        if values[0] > 800 :
            print("%s %d (안전)" % (timestamp, values[0]))
        elif values[0] > 500 :
            print("%s %d (주의)" % (timestamp, values[0]))
        else :
            print("%s %d (화재 경보)" % (timestamp, values[0]))
        
        time.sleep(1)