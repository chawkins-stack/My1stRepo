def calculate_tip(value):
    bill = value

    tip = bill * 0.15 if 50 <= bill <= 300 else bill * 0.20
    total_value = bill + tip

    return f"The bill was ${bill}, the tip was ${tip}, and the total value ${total_value}"


print(calculate_tip(275))
print(calculate_tip(40))
print(calculate_tip(430))