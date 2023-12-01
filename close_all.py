import sys
import serial
sys.path.append('/home/linaro/hottub_ma/plc/')
from modbus import Modbus
sys.path.append('/home/linaro/hottub_ma/relay/')
from modbus_relay import Modbus_relay
sys.path.append('/home/linaro/hottub_ma/setting/')
from path_url import Path_url


plc_mod = Modbus()
relay_mod = Modbus_relay()
path_url = Path_url()

class Close_All():
    def start_close_plc(self, plc):
        if plc[0] == True:
            try:
                send = serial.Serial(
                    port=path_url.modbus_port,
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)
                data_bytes = bytes([path_url.plc_address,0x05,0x26,0x00,0x00,0x00,0xC6,0x82])
                send.write(data_bytes)
                # send.write(b"\x01\x05\x26\x00\x00\x00\xC6\x82")
                send.close()
            except:
                pass
        if plc[0] == False:
            if plc[1] == True:
                try:
                    ozone = serial.Serial(
                        port=path_url.modbus_port,
                        baudrate = 9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)
                    data_bytes = bytes([path_url.plc_address,0x05,0x26,0x01,0x00,0x00,0x97,0x42])
                    ozone.write(data_bytes)
                    # ozone.write(b"\x01\x05\x26\x01\x00\x00\x97\x42")
                    # ozone.close()
                except:
                    pass
        if plc[1] == False:
            if plc[2] == True:
                try:
                    send = serial.Serial(
                        port=path_url.modbus_port,
                        baudrate = 9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)
                    data_bytes = bytes([path_url.plc_address,0x05,0x26,0x02,0x00,0x00,0x67,0x42])
                    send.write(data_bytes)
                    # send.write(b"\x01\x05\x26\x02\x00\x00\x67\x42")
                except:
                    pass

    def start_close_relay(self, relay):
        if relay[0] == True:
            relay_mod.close_lamp_ozone()
        if relay[0] == False:
            relay_mod.close_lamp_uv()
        if relay[1] == False:
            relay_mod.close_pompe_air()
        if relay[2] == False:
            relay_mod.close_besgo()
        if relay[3] == False:
            relay_mod.close_ph()
        if relay[4] == False:
            relay_mod.close_orp()
        if relay[5] == False:
            relay_mod.close_apf()
            

