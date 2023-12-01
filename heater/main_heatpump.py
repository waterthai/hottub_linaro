import json
import sys
from urllib.request import urlopen
from modbus_heater import Modbus_heatpump
sys.path.append('/home/linaro/hottub_ma/relay/')
from modbus_relay import Modbus_relay
sys.path.append('/home/linaro/hottub_ma/setting/')
from path_url import Path_url
sys.path.append('/home/linaro/hottub_ma/plc/')
from modbus import Modbus


path_url = Path_url()
url_setting = path_url.url_setting
url = path_url.url_setting_mode
mod_heatpump = Modbus_heatpump()
modbus_relay  = Modbus_relay()
plc_mod = Modbus()


class Main_heatpump():
    def start_heatpump(self,  temperature, plc, relay_8):
        if plc[2] == True:
            mod_heatpump.stop_chauffage()
        if relay_8[4] == False:
            response_setting = urlopen(url_setting)
            data_setting = json.loads(response_setting.read())

            setting = urlopen(url)
            data_mode = json.loads(setting.read())
            if str(data_mode[0]['sm_filtration']) != "0":
                if str(data_mode[0]['sm_chauffage']) == "1" and plc[0] == True:
                    set_temp = float(data_setting[0]['setting_temperature'])
                    temp_div = float(data_setting[0]['setting_temp_deff'])
                    read = float(temperature)
                    print(set_temp)
                    print(temp_div)
                    print(read)

                    # minus = float(data_setting[0]['setting_temperature']) - float(data_setting[0]['setting_temp_deff'])
                    if  float(data_setting[0]['setting_temperature']) - float(data_setting[0]['setting_temp_deff']) >=  float(temperature):
                        print("เปิดปั้ม")
                        read_status_auto = open('/home/linaro/hottub_ma/txt_file/status_working_heater.txt','w')
                        read_status_auto.write("True")
                        if relay_8[7] == False:
                            mod_heatpump.open_heatpump()
                    elif float(temperature) >= float(data_setting[0]['setting_temperature']): 
                        print("ปิดปั้ม")
                        read_status_auto = open('/home/linaro/hottub_ma/txt_file/status_working_heater.txt','w')
                        read_status_auto.write("False")
                        if relay_8[7] == True:
                            mod_heatpump.close_heatpump()
                elif str(data_mode[0]['sm_chauffage']) == "1" and plc[0] == False:
                    set_temp = float(data_setting[0]['setting_temperature'])
                    temp_div = float(data_setting[0]['setting_temp_deff'])
                    read = float(temperature)
                    print(set_temp)
                    print(temp_div)
                    print(read)
                    if float(data_setting[0]['setting_temperature']) - float(data_setting[0]['setting_temp_deff']) >  float(temperature):
                        read_status_auto = open('/home/linaro/hottub_ma/txt_file/status_working_heater.txt','w')
                        read_status_auto.write("True")
                        if plc[0] == False:
                            plc_mod.start_filtration()
                    else :
                        print("ปิดปั้ม")
                        read_status_auto = open('/home/linaro/hottub_ma/txt_file/status_working_heater.txt','w')
                        read_status_auto.write("False")
                        if relay_8[7] == True:
                            mod_heatpump.close_heatpump()
                else:
                    read_status_auto = open('/home/linaro/hottub_ma/txt_file/status_working_heater.txt','w')
                    read_status_auto.write("False")
                    if relay_8[7] == True:
                        mod_heatpump.close_heatpump()
            else:
                read_status_auto = open('/home/linaro/hottub_ma/txt_file/status_working_heater.txt','w')
                read_status_auto.write("False")
                if relay_8[7] == True:
                    mod_heatpump.close_heatpump()

        else:
            read_status_auto = open('/home/linaro/hottub_ma/txt_file/status_working_heater.txt','w')
            read_status_auto.write("False")
            if relay_8[7] == True:
                mod_heatpump.close_heatpump()
                
            if relay_8[7] == False:
                if plc[1] == True:
                    mod_heatpump.stop_pump_ozone()


        
