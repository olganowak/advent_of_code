with open("input.txt") as f:
    banks = [bank.strip() for bank in f.readlines()]

joltages = []
for bank in banks:
    bank2 = 0
    for i, battery in enumerate(bank):
        b = int(battery)
        if i == 0:
            bank1 = b
        elif i != len(bank) - 1:
            if b > bank1:
                bank1 = b
                bank2 = 0
            elif b > bank2:
                bank2 = b
        else:
            if b > bank2:
                bank2 = b
    joltage = int(str(bank1) + str(bank2))
    joltages.append(joltage)

print("Result 1:", sum(joltages))

def numbers_before(voltage, bank, i):
    numbers_before = 0
    s = 0
    for number in bank[:i+1]:
        try:
            value = voltage[s]
        except IndexError:
            return numbers_before

        if number == voltage[s]:
            numbers_before += 1
            s += 1
    return numbers_before


def new_voltage(bank, i, voltage):
    b = int(bank[i])
    if len(bank) - i >= 12:
        for i2, b2 in enumerate(voltage):
            b2  = int(b2)
            if b > b2 and i2 < numbers_before(voltage, bank, i):
                voltage = voltage[:i2]+bank[i:i+12-i2]
                return voltage
    else:
        for i2, b2 in enumerate(voltage):
            b2 = int(b2)
            if b > b2 and i2 < numbers_before(voltage, bank, i):
                if len(voltage[:i2] + bank[i:i+12-i2]) == 12:
                    voltage = voltage[:i2]+bank[i:i+12-i2]
                    return voltage
    return voltage

voltages = []
for bank in banks:
    for i in range(len(bank)):
        if i == 0:
            voltage = bank[:12]
        else:
            voltage = new_voltage(bank, i, voltage)
    voltages.append(int(voltage))

print("Result 2:", sum(voltages))
