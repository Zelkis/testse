i = 0 
j1= 1
j2= 2
j3 = 3
def pega_parte_decimal(x):
    while x>=1:
        x-=1
        x=round(x*10)/10
    return x
    
while i <= 2 :
    print(f'I={i} J={j1}')
    print(f'I={i} J={j2}')
    print(f'I={i} J={j3}')
    i+=0.2
    i = round(10*i)/10
    j1+=0.2
    j2+=0.2
    j3+=0.2
    j1=round(j1*10)/10
    j2= round(j2*10)/10
    j3 =round(j3*10)/10
    if pega_parte_decimal(i) == 0:
        i=int(i)
    if pega_parte_decimal(j1) == 0:
        j1 = int(j1)
    if pega_parte_decimal(j2) == 0:
        j2 = int(j2)
    if pega_parte_decimal(j3) == 0:
        j3 = int(j3)
        
        