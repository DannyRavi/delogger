
#
#DETAIL OF COMPONENTS
#
Hmc = 0.0001

Nrf_standby = 0.000022
Nrf_Tx = 0.0113
Nrf_Rx = 0.0123
Nrf_PowerDown = 0.0000009

arduino_nano_Hmc_nrf_led_16Mhz = 0.0224
atmega328_max_Cry20Mhz_5V = 0.012
atmega328_min_Rc1Mhz_2V = 0.0003
stm8L_normal = 0.000003
stm8L_veryLow = 0.00000035

Battry_Current_mAh = 2.2
Battry_volt = 3.3


#
#! SUM CONSUME   STM8L151K4T6 = 15 - 20
# atmega 16  /  stm32f103c8 / 
# STM8L151K4T6 = 15 - 20  / 


All_max_component_AT328 = ((Nrf_Tx / 3600)) + Hmc + \
    atmega328_max_Cry20Mhz_5V + Nrf_standby
All_min_component_AT328 = ((Nrf_Tx / 3600)) + Hmc + \
    atmega328_min_Rc1Mhz_2V + Nrf_standby
stm8L_normal_component = ((Nrf_Tx / 3600)) + Hmc + stm8L_normal + Nrf_standby
stm8L_veryLow_componen = ((Nrf_Tx / 3600)) + Hmc + stm8L_veryLow + Nrf_standby



# FUCTION AND PRIND DATA



def consumer_days(time_consume):
    cunsomer = time_consume
    Consume_day = cunsomer * 24
    counsume_during_days = Battry_Current_mAh / Consume_day
    return counsume_during_days


# print(Consume_day, "mA")
print(consumer_days(arduino_nano_Hmc_nrf_led_16Mhz),
      "days ==> arduino_nano_Hmc_nrf_led_16Mhz")
print(consumer_days(All_max_component_AT328),
      "days ==> AT328_All_max_component_AT328")
print(consumer_days(All_min_component_AT328),
      "days ==> AT328_All_min_component")
print(consumer_days(stm8L_normal_component), "days ==> stm8L_normal_component")
print(consumer_days(stm8L_veryLow_componen), "days ==> stm8L_veryLow_componen")

#
# # !CONCLUDE
#

# with Arduino = 4.092261904761905, 'days
# All_max_component = 7.560050858523958, 'days'
# All_min_component = 215.61581182620066, 'days'
# stm8L_normal_component = 715.3696076306092, 'days'
# stm8L_veryLow = 730.476359128741, 'days'

#
# #!REFRECES
#


# Based on the datasheet (fig 30-8, p 319), I would say the the processor will draw around 2.4 mA at 5 volts.
# https://electronics.stackexchange.com/questions/247456/what-is-the-best-way-to-estimate-the-power-consumption-of-an-atmega328p-microcon
# https://www.st.com/en/microcontrollers/stm8l-series.html?querycriteria=productId=SS1336
# https://www.st.com/content/st_com/en/products/microcontrollers/stm8-8-bit-mcus/stm8l-series/stm8l151-152/stm8l152k4.html


print("amp",All_min_component_AT328)