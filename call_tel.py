n=int(input("Введите число минут:"))
code=int(input("Введите код города"))

if code==343:
    return 15*n
elif code==381:
    return 18*n
elif code==473:
    return 13*n
elif code==485:
    return 11*n
else:
    print('wrong code')
