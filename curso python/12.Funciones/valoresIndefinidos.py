def parametro(*num):
    for i in num:
        print(i)
    return type(num)
    

print(parametro(16 , 17 , 18 , 19 , 20))