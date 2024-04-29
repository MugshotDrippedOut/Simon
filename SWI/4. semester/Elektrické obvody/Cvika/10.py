import math
import matplotlib.pyplot as plt

p = 10.1
Rwi = 5.4
Ra = 6.4


# Mereni naprazdno
U10 = [235, 224.4, 214.6, 205, 194.5, 184.8]
I0 = [84.6, 72, 62.6, 54.4, 46.6, 40.4]
I0 = [i/1_000 for i in I0] # mA -> A
deltaP = [3,2.5,2.4,2,1.8,1.5]

def Z0(U10, I0):
    return U10/I0

def deltaPwa(I,Rwi, Ra):
    return I**2 * (Rwi + Ra)

def deltaP0(deltaP, deltaPwa):
    return deltaP - deltaPwa

def cos0(P, I, U):
    return P/(I*U)

def I0p(I, cos0):
    return I * cos0

def I0q(I0, I0p):
    return (I0**2 - I0p**2)**0.5

def deltaPj(I):
    return I**2 * 41.5

def deltaPfe(deltaP0, deltaPj):
    return deltaP0 - deltaPj

Z0_res = [Z0(U10[i], I0[i]) for i in range(len(U10))]
deltaPwa_res = [deltaPwa(I0[i], Rwi, Ra) for i in range(len(U10))]
deltaP0_res = [deltaP0(deltaP[i], deltaPwa_res[i]) for i in range(len(U10))]
cos0_res = [cos0(deltaP0_res[i], I0[i], U10[i]) for i in range(len(U10))]
I0p_res = [I0p(I0[i], cos0_res[i]) for i in range(len(U10))]
I0q_res = [I0q(I0[i], I0p_res[i]) for i in range(len(U10))]
deltaPj_res = [deltaPj(I0[i]) for i in range(len(U10))]
deltaPfe_res = [deltaPfe(deltaP0_res[i], deltaPj_res[i]) for i in range(len(U10))]

def Mereni_naprazdno():
    print(f"{'U10':<10}{'I0 [mA]':<10}{'deltaP':<10}{'Z0':<10}{'deltaPwa':<10}{'deltaP0':<10}{'cos0':<10}{'I0p [mA]':<10}{'I0q [mA]':<10}{'deltaPj':<10}{'deltaPfe':<10}")
    for i in range(len(U10)):
        print(f"{U10[i]:<10.4g}{I0[i]*1000:<10.4g}{deltaP[i]:<10.4g}{Z0_res[i]:<10.4g}{deltaPwa_res[i]:<10.4g}{deltaP0_res[i]:<10.4g}{cos0_res[i]:<10.4g}{I0p_res[i]*1000:<10.4g}{I0q_res[i]*1000:<10.4g}{deltaPj_res[i]:<10.4g}{deltaPfe_res[i]:<10.4g}")


# Mereni nakratko
Uk = [79.8,74.7,69.6,64.7,59.5,55.4,50.2,44.7]
Ik = [0.55,0.5,0.46,0.42,0.39,0.36,0.33,0.29]
deltaPk = [44,38,32.5,28,23.5,20,16.5,13]

Zk_res = [Z0(Uk[i], Ik[i]) for i in range(len(Uk))]
cos0k_res = [cos0(deltaPk[i], Ik[i], Uk[i]) for i in range(len(Uk))]

def Mereni_nakratko():
    print(f"{'Uk':<10}{'Ik':<10}{'deltaPk':<10}{'Zk':<10}{'cos0k':<10}")
    for i in range(len(Uk)):
        print(f"{Uk[i]:<10.4g}{Ik[i]:<10.4g}{deltaPk[i]:<10.4g}{Zk_res[i]:<10.4g}{cos0k_res[i]:<10.4g}")


def new_line(N = 1):
    for _ in range(N):
        print("")

U2n = 22
I1k = [0.55,0.5,0.46,0.42]
Pjk = [44,38,32.5,28]

def I2(p, I):
    return p*I

def rS(I2, U2n):
    return U2n*I2

# Vypocet ucinosti transformatoru
I2_res = [I2(p, I1k[i]) for i in range(len(I1k))]
rS_res = [rS(I2_res[i], U2n) for i in range(len(I1k))]
cos05_res = [0.5*rS_res[i] for i in range(len(I1k))]
cos08_res = [0.8*rS_res[i] for i in range(len(I1k))]
cos1_res = [rS_res[i] for i in range(len(I1k))]

def Vut():
    print(f"{'rS':<10}{'I2 []':<10}{'I1k':<10}{'Pjk':<10}{'cos05':<10}{'cos08':<10}{'cos1':<10}")
    for i in range(len(I1k)):
        print(f"{rS_res[i]:<10.4g}{I2_res[i]:<10.4g}{I1k[i]:<10.4g}{Pjk[i]:<10.4g}{cos05_res[i]:<10.4g}{cos08_res[i]:<10.4g}{cos1_res[i]:<10.4g}")




Mereni_naprazdno()
new_line(2)
Mereni_nakratko()
new_line(2)
Vut()

# Grafy
# Zavislost X na Y a rozdelenie do 8 subgrafu s ruznymi titles a labels

lablesNaprazdno = ["Závislost příkonu naprázdno na napětí naprázdno", "Závislost proudu naprázdno na napětí naprázdno", "Závislost účiníku naprázdno na napětí naprázdno"]
labelsNakratko = ["Závislost příkonu nakrátko na napětí nakrátko", "Závislost proudu nakrátko na napětí nakrátko", "Závislost účiníku nakrátko na napětí nakrátko", "Závislost příkonu nakrátko na proudu nakrátko"]
label3 = "Závislost napětí transformátoru U2 na velikosti odebíraného proudu I2"

labels = []
def appentTo(labels, arr):
    for i in arr:
        labels.append(i)
appentTo(labels, lablesNaprazdno)
appentTo(labels, labelsNakratko)
appentTo(labels, [label3])

def plot(X, Y, labels):
    plt.subplot(4,2,1)
    plt.plot(X[0], Y[0], '-bo')
    plt.title(labels[0])
    plt.xlabel('U10 [V]')
    plt.ylabel('ΔP [W]')
    plt.grid(True)
    
    for i in range(1,3):
        plt.subplot(4,2,i+1)
        plt.plot(X[i], Y[i], '-bo')
        plt.title(labels[i])
        match i:
            case 1:
                plt.xlabel('U10 [V]')
                plt.ylabel('I0 [A]')
            case 2:
                plt.xlabel('U10 [V]')
                plt.ylabel('cosφ0 [°]')
        plt.grid(True)
        
    for i in range(3,7):
        plt.subplot(4,2,i+1)
        plt.plot(X[i], Y[i], '-bo')
        plt.title(labels[i])
        match i:
            case 3:
                plt.xlabel('Uk [V]')
                plt.ylabel('ΔPk [W]')
            case 4:
                plt.xlabel('Uk [V]')
                plt.ylabel('Ik [A]')
            case 5:
                plt.xlabel('Uk [V]')
                plt.ylabel('cosφk [°]')
            case 6:
                plt.xlabel('Ik [A]')
                plt.ylabel('ΔPk [W]')
        plt.grid(True)
    
    plt.subplot(4,2,8)
    plt.plot(X[7], Y[7], '-bo')
    plt.title(labels[7])
    plt.xlabel('I2 [A]')
    plt.ylabel('U2n [V]')
    plt.grid(True)
    
    plt.subplots_adjust(hspace = 0.9, wspace = 0.5)
    
    plt.show()

U2 = [21.78,22.1,22.28,22.42,22.56,22.67]
I2_ = [1.1,0.9,0.8,0.7,0.6,0.5]
X = [U10, U10, U10, Uk, Uk, Uk, Ik, I2_]
Y = [deltaP, I0, cos0_res, deltaPk, Ik, cos0k_res, deltaPk, U2]
plot(X, Y, labels)