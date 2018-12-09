salario = input()
result = 0
if salario > 0 or salario <= 12450:
    result = salario * 0.19
    print result
elif salario > 12450 or salario <= 20200:
    result = salario * 0.24
    print result
elif salario > 20200 or salario <= 35200:
    result = salario * 0.30
    print result
elif salario > 35200 or salario <= 60000:
    result = salario * 0.37
    print result
elif salario > 60000:
    result = salario * 0.45
    print result