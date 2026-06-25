def calculate_tip(value):
    tip = value * 0.15 if value >= 50 and value <= 300 else value * 0.20

    total_value = value + tip

    return f"The bill was ${value}, the tip was ${tip}, and the total value ${total_value}"


print(calculate_tip(275))
print(calculate_tip(40))
print(calculate_tip(430))