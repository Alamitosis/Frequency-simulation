import pyvisa
import time 

rm=pyvisa.ResourceManager()
rm.list_resources()
my_instrument = rm.open_resource('USB0::0X0699::0x0353::1725542::0::INSTR')
print(my_instrument.query('*IDN?'))

for i in range (5,11,1):
    my_instrument.write("OUTP1:STAT OFF")
    time.sleep(5)
    my_instrument.write("SOUR1:FREQ"+str(i*0.01)+"Hz")
    my_instrument.write("OUTP1:STAT ON")
    time.sleep(25)

for i in range (2,11,1):
    my_instrument.write("OUTP1:STAT OFF")
    time.sleep(5)
    my_instrument.write("SOUR1:FREQ"+str(i*0.1)+"Hz")
    my_instrument.write("OUTP1:STAT ON")
    time.sleep(6)
    
for i in range (2,121,1):
    my_instrument.write("OUTP1:STAT OFF")
    time.sleep(5)
    my_instrument.write("SOUR1:FREQ"+str(i)+"Hz")
    my_instrument.write("OUTP1:STAT ON")
    time.sleep(1)
    
my_instrument.close()