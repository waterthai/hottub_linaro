import minimalmodbus
import serial
import sys
from pymodbus.client import ModbusSerialClient
sys.path.append('/home/linaro/hottub_linaro/setting/')
from path_url import Path_url

path_url = Path_url()

class Modbus():
    def read_status_relay(self):
        status_relay = []
        client1 = ModbusSerialClient(
                method='rtu',
                port=path_url.modbus_port,
                baudrate=9600,
                timeout=3,
                parity='N',
                stopbits=1,
                bytesize=8
            )
        client1.connect()
        res1 = client1.read_coils(0, 8, path_url.relay_address)
        status_relay.append(res1.bits[0])
        status_relay.append(res1.bits[1])
        status_relay.append(res1.bits[2])
        status_relay.append(res1.bits[3])
        status_relay.append(res1.bits[4])
        status_relay.append(res1.bits[5])
        status_relay.append(res1.bits[6])
        status_relay.append(res1.bits[7])
        return status_relay   

    def read_status_plc_out(self):
        status_plc_out = []
        client = ModbusSerialClient(
                method='rtu',
                port=path_url.modbus_port,
                baudrate=9600,
                timeout=3,
                parity='N',
                stopbits=1,
                bytesize=8
            )
        client.connect()
        res = client.read_coils(512, 4,path_url.plc_address)
        status_plc_out.append(res.bits[0])
        status_plc_out.append(res.bits[1])
        status_plc_out.append(res.bits[2])
        status_plc_out.append(res.bits[3])
        return status_plc_out
    
   
        
    def start_filtration(self):
        try:
            send = serial.Serial(
                port=path_url.modbus_port,
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            data_bytes = bytes([path_url.plc_address,0x05,0x26,0x00,0xFF,0x00,0x87,0x72])
            send.write(data_bytes)
            # send.write(b"\x01\x05\x26\x00\xFF\x00\x87\x72")
            send.close() 
        except:
            pass


    def stop_filtration(self):
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

    def start_ozone_pump(self):
            ozone = serial.Serial(
                port=path_url.modbus_port,
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            # data_bytes = bytes([path_url.plc_address,0x05,0x26,0x01,0xFF,0x00,0xD6,0xB2])
            # ozone.write(data_bytes)
            ozone.write(b"\x01\x05\x26\x01\xFF\x00\xD6\xB2")
            ozone.close()
 

    def stop_ozone_pump(self):
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

    def start_chauffage(self):
        try:
            send = serial.Serial(
                port=path_url.modbus_port,
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            data_bytes = bytes([path_url.plc_address,0x05,0x26,0x02,0xFF,0x00,0x26,0xB2])
            send.write(data_bytes)
            # send.write(b"\x01\x05\x26\x02\xFF\x00\x26\xB2")
        except:
            pass

    def stop_chauffage(self):
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
    def start_chauffage2(self):
        try:
            send = serial.Serial(
                port=path_url.modbus_port,
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            data_bytes = bytes([path_url.plc_address,0x05,0x26,0x03,0xFF,0x00,0x77,0x72])
            send.write(data_bytes)
            # send.write(b"\x01\x05\x26\x03\xFF\x00\x77\x72")
        except:
            pass

    def stop_chauffage2(self):
        try:
            send = serial.Serial(
                port=path_url.modbus_port,
                baudrate = 9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1)
            data_bytes = bytes([path_url.plc_address,0x05,0x26,0x03,0x00,0x00,0x36,0x82])
            send.write(data_bytes)
            # send.write(b"\x01\x05\x26\x03\x00\x00\x36\x82")
        except:
            pass
    
    def read_temp(self):
        instrument = minimalmodbus.Instrument(path_url.modbus_port,path_url.plc_address)
        instrument.serial.port                     # this is the serial port name
        instrument.serial.baudrate = 9600         # Baud
        instrument.serial.bytesize = 8
        instrument.serial.parity   = serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.serial.timeout  = 1  
        return instrument.read_register(18179)


