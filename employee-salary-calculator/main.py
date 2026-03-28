'''employee salary calculator'''

# calculating hra 
def get_hra(basic):
    hra= 0.20* basic
    return hra

# calculating da 
def get_da(basic):
    da= 0.10* basic
    return da

#claculating gross salary 
def get_gross(basic,hra,da):
    gross= basic+hra+da
    return gross

##calculating tax amount 
def get_tax(gross):
    amt= 0.05*gross
    return amt

#calculating net salary 
def salary(gross,tax):
    net_salary=gross-tax
    return net_salary

#show calculation summary 
def show(name,basic,hra,da,gross,tax,net):
    print('\n-----SALARY CHART-----\n')
    print(f'name:{name}\n')
    print(f'Basic salary:{basic}\n')
    print(f'HRA(20%):{hra}\n')
    print(f'DA(10%):{da}\n')
    print(f'Gross salary:{gross}\n')
    print(f'Tax amount (5%):{tax}\n')
    print(f'Net salary:{net}\n')

#main code

name=input("enter your name: ")

basic=int(input("enter your salary: "))

hra= get_hra(basic)

da= get_da(basic)

gross= get_gross(basic,hra,da)

tax= get_tax(gross)

net= salary(gross,tax)

show(name,basic,hra,da,gross,tax,net)
