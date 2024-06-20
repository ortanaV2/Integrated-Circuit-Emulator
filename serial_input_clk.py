from machine import Pin
import time

auto_clk = Pin(5, Pin.OUT)
clk = Pin(2, Pin.IN) #GPIO2 -> D4
serial_output = Pin(0, Pin.OUT) #binary data output
true_output = Pin(4, Pin.OUT) #true data flow signal bit
bin_data = open("assembly.bin").read()
bin_data_len = len(bin_data)
data_state = 0

true_output.value(0)
serial_output.value(0)

reset_button = False
clock_count = 0
clock_speed = 0.5

##########
# Clock hat negative Datenumschalt-Flanke
# True Output = 1 signalisiert das es einen Dateneinfluss (Übertragung) gibt.
# Serieller Output ist synchron zur Clock Flanke.
##########

while True:
    clock_count += 1
    if clock_count % 2 == 0:
        auto_clk.value(1)
    else:
        auto_clk.value(0)
    if clk.value() == 0 and not reset_button:
        reset_button = True
        print("CLK - Request: " + str(clock_count))
        if data_state != bin_data_len:
            true_output.value(1)
            serial_output.value(int(bin_data[data_state]))
            data_state += 1
            print("Send bit")
        else:
            true_output.value(0)
            serial_output.value(0)
    if clk.value() == 1 and reset_button:
        reset_button = False
    time.sleep(clock_speed)
