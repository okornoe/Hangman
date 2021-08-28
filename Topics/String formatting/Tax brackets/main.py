income = int(input())
percentage = 0
taxable = 0

if 0 <= income <= 15527:
    percentage = 0
    taxable = 0
elif 15528 <= income <= 42707:
    percentage = 15
    taxable = 0.15 * income
elif 42708 <= income <= 132406:
    percentage = 25
    taxable = 0.25 * income
elif income >= 132407:
    percentage = 28
    taxable = 0.28 * income
print("The tax for {} is {}%. That is {:.0f} dollars!".format(income, percentage, taxable))
