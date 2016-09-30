import numpy as np
import matplotlib.pyplot as plt
import random as r


N=20 #lado de la red
NxN=N**2
JKBT=np.arcsinh(1)/2.0
time=100000
T=JKBT*np.linspace(0.8  ,1.6,15)#se define un arreglo de 10 posibles temperaturas para trabajar en la red
T_no_units=1/T
print("Lado de la red N="+str(N)+"\n")
print("Tamaño de la red NxN=" +str(NxN)+"\n")
print("J/K_BT="+str(JKBT)+"\n")
print("Tiempo de simulación t="+str(time))
print("Arreglo de posibles J/K_BT")
print(T)
A=np.zeros(NxN)

#se genera una configuracion de spins al azar



#esta es la funcion de energia
def Energia(A,N,JKBT):
    E=0
    for i in range(N):
        for j in range(N):
            a1=(i+1)%N
            a2=(i-1)%N
            b1=(j+1)%N
            b2=(j-1)%N
            E+=A[N*i+j]*( A[N*a1+j]+  A[N*a2+j]+  A[N*i+b1] + A[N*i+b2] )
    return -E*JKBT

#Esta función calcula la magnetizacion promedio del sistema, dado que m=<s> podemos simplemente sumar sobre los spins obtenidos y promediar sobre el número de spins de la red
def Magne(A,NxN):
    suma=0.0
    for i in range(NxN):
        suma+=A[i]
    return suma/NxN


print("\n\n\n\n\n %%%%%%%%%%%%%%%%%%%%%%%% COMENZANDO SIMULACIÓN %%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\n\n\n\n")


ENERGY=np.zeros(time)
Magn=np.zeros(len(T))

for l in range(len(T)):
    print("Posición número ",l, "de ",len(T))
    
    for k in range(NxN):
        a=r.random()
        if(a>0.5):
            A[k]=1
        if(a<0.5):
            A[k]=-1

    
    
    for i in range(time):
    
        b=r.random()
        s=int(b*NxN) #spin que sera volteado
        des=0
        B=A.copy()#NewMatrix(A,s,NxN) #se define la matriz de cambio
    
    
        E_t=0#energia que se tiene en el paso
    
    
        E1=Energia(A,N,JKBT)#energia matriz A
        
        E_t=E1#se da como la energia en este tiempo la energia del sistema A


        if (B[s]==-1 and des==0):
            B[s]=1
            des=1
          
        if(B[s]==1 and des==0):
            B[s]=-1
            des=1

        E2=Energia(B,N,JKBT)#energia matriz B
    
        #en este punto se decide si se cambia el spin dado
        if(E2-E1<=0):
            A=B
            E_t=E2
        #si el cambio de energia fue positivo
        if((E2-E1)>0):
            p=r.random()
            ind=l
            d=np.exp(-T[ind]*(E2-E1))
            #se hace el algoritmo montecarlo con una probabilidad d de hacer el salto
            if(p<d):
                A=B
                E_t=E2
        if(l==9):
            ENERGY[i]=E_t#se guarda la energia de este paso del sistema

    print("Magnetizacion=",Magne(A,NxN))
    
    Magn[l]=Magne(A,NxN)#aqui esta la magnetización de este sistema a la temperatura l
    '''
    #Este codigo fue utilizado para graficar la energia en la temperatura final
    if(l==9):
        plt.plot(ENERGY)
        plt.ylabel("$ E/K_B T $",size=20)
        plt.xlabel("$ simulation\ time $",size=20)
        plt.savefig("Energia_en_t.png")
        plt.show()
        plt.close()
    '''

#invierte los arreglos
#T_no_units=T_no_units[::-1]
#Magn=Magn[::-1]
print("T_no_units",T_no_units)
print("Magn",Magn)


plt.scatter(T_no_units,Magn)
plt.ylabel("$  < m > $",size=20)
plt.xlabel("$ k_B T/J $",size=20)
plt.savefig("Magne.png")
plt.show()
plt.close()




















