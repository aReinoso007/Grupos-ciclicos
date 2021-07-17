def generadores(n):
    s = set(range(1, n))
    print('S: ', s)
    r = []
    for a in s:
        g = set()
        for x in s:
            g.add((a**x) % n)
        if g == s:
            r.append(a)
    return r

def verificar():
    n = int(input("Valor de Z: "))
    gndrs = generadores(n)
    if(len(gndrs)!=0):
        print('Grupo es finito ciclico')
    else:
        print('No es un grupo finito ciclico')
    if gndrs:
        print(f"Z_{n} tiene los generadores {gndrs}")
    group=range(1,n)
    for x in gndrs:
        print("--------------")
        print("GENERADOR  ",x)
        print("--------------")
        for i in group:
            res= (x**i)%n
            print(x,"^",i,"mod",n,"=",res)
        print("------------")

verificar()