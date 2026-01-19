from instruments import hcp
import time

inst = hcp.TC038D.open_serial('COM3')

target = float(input('Please, insert the desired final temperature: '))
step = float(input('Please, insert in Celsius what should be the step of the increase: '))
second = float(input('Please, insert how much time you need per step: '))

temperature = inst.temperature

while temperature.magnitude != target:
    if temperature.magnitude > target: #safety sequence
        inst.setpoint = target
        break
    else:
        temperature = inst.temperature
        temp = temperature.magnitude + step
        inst.setpoint = temp 
        while temperature.magnitude != temp:
            time.sleep(1)
            temperature = inst.temperature
        time.sleep(second)
