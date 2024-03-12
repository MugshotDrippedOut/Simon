import matplotlib.pyplot as plt
import numpy as np

# Napetovy delič tvořený malými hodnotami odporů
prveU = 5
prveRv = 10_000_000
prveR1 = 1_000
prveR2 = [1_000, 2_000, 9_000, 10_000, 49_000, 50_000, 199_000, 200_000]
prveUr1 = [2.5, 1.67, 0.5, 0.456, 0.1, 0.098, 0.025, 0.025]
prveUr2 = [2.5, 3.34, 4.5, 4.55, 4.9, 4.91, 4.98, 4.98]

# napetovy delič tvořený odpory srovnatelnými s vnitřním odporem voltmetru
druheU = 1.5
druheRv = [10_000_000, 10_000_000_000, 10_000_000, 10_000_000_000]
druheR1 = [100_000, 100_000, 1_000_000, 1_000_000]
druheR2 = [100_000, 100_000, 1_000_000, 1_000_000]
druheUr1 = [0.751, 0.748, 0.754, 0.719]
druheUr2 = [0.749, 0.753, 0.746, 0.782]

# prve merania
merania1 = []
for i in range(len(prveR2)):
    meranie = {
        "Uv": prveU,
        "Rv": prveRv,
        "R1": prveR1,
        "R2": prveR2[i],
        "Ur1": prveUr1[i],
        "Ur2": prveUr2[i]
    }
    merania1.append(meranie)

# druhe merania
merania2 = []
for i in range(len(druheRv)):
    meranie = {
        "Uv": druheU,
        "Rv": druheRv[i],
        "R1": druheR1[i],
        "R2": druheR2[i],
        "Ur1": druheUr1[i],
        "Ur2": druheUr2[i]
    }
    merania2.append(meranie)
    
# grafy - zatizovaci primku nahradniho zdroje napeti
def generuj_graf1(merania1,merania2):
    x = [i["R2"]/1000 for i in merania1]
    y1 = [i["Ur1"] for i in merania1]
    y2 = [i["Ur2"] for i in merania1]
    plt.subplot(1,2,1)
    plt.plot(x, y1, '-ro', label='UR1')
    plt.plot(x, y2, '-bo', label='UR2')
    plt.title('Napetovy delič s velkými odpory')
    plt.xlabel('R2 [kΩ]')
    plt.ylabel('UR [V]')
    plt.grid(True)
    plt.legend()

    
    x = [i["R2"]/1000 for i in merania2]
    y1 = [i["Ur1"] for i in merania2]
    y2 = [i["Ur2"] for i in merania2]
    plt.subplot(1,2,2)
    plt.plot(x, y1, 'go', label='UR1')
    plt.plot(x, y2, 'bo', label='UR2')
    for i in range(len(x)):
        Rv = (str(merania2[i]["Rv"]/1_000_000_000)[:-2] + " GΩ" if merania2[i]["Rv"]/1_000_000 >= 1000 else str(merania2[i]["Rv"]/1_000_000)[:-2] + " MΩ")
        plt.text(x[i], y1[i], f'Rv={Rv}', fontsize=6, ha='right')
        plt.text(x[i], y2[i], f'Rv={Rv}', fontsize=6, ha='right')
    plt.title('Napetovy delič s odpory srovnatelnými s vnitřním odporem voltmetru')
    plt.xlabel('R2 [kΩ]')
    plt.ylabel('UR [V]')
    plt.grid(True)
    plt.legend()
    plt.show()


generuj_graf1(merania1, merania2)
    

