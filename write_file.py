
class Write_file():


    def start_write(self, relay_8, plc_status, temperature, ph, orp, pressure, plc_in):
        print("writefile open")
        relay_file = open('/home/linaro/hottub_ma/txt_file/status_relay_8.txt','w')
        relay_file.write(str(relay_8))

        plc_file = open('/home/linaro/hottub_ma/txt_file/status_plc.txt','w')
        plc_file.write(str(plc_status))

        plc_file_in = open('/home/linaro/hottub_ma/txt_file/status_plc_in.txt','w')
        plc_file_in.write(str(plc_in))

        temperature_file = open('/home/linaro/hottub_ma/txt_file/temperature.txt','w')
        temperature_file.write(str(temperature))


        ph_file = open('/home/linaro/hottub_ma/txt_file/ph.txt','w')
        ph_file.write(str(ph))
        
        orp_file = open('/home/linaro/hottub_ma/txt_file/orp.txt','w')
        orp_file.write(str(orp))

        pressure_file = open('/home/linaro/hottub_ma/txt_file/pressure.txt','w')
        pressure_file.write(str(pressure))
        print("writefile close")

    def write_over_presssure(self,pressure):
        print("writefile pressure open")
        pressure_file = open('/home/linaro/hottub_ma/txt_file/count_down_close_system.txt','w')
        pressure_file.write(str(pressure))
        print("writefile pressure close")

    def clear_pressure_time(self):
        count_down_read = open('/home/linaro/hottub_ma/txt_file/count_down_close_system.txt','w')
        count_down_read.write('')

