import random
import matplotlib.pyplot as plt



def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(zoznam):
    novy_zoznam = zoznam.copy()
    for i in range(len(zoznam)):
        minimum = min(novy_zoznam[i:])
        min_index = i
        for j in range(i, len(novy_zoznam)):
            if novy_zoznam[j] == minimum:
                min_index = j
                break
        novy_zoznam[i], novy_zoznam[min_index] = novy_zoznam[min_index], novy_zoznam[i]
    return novy_zoznam


def bubble_sort(zoznam):
    novy_zoznam = zoznam.copy()
    plt.ion()
    plt.show()
    while True:
        zmena = 0
        for i in range(len(zoznam)-1):
            index_highlight1 = i
            index_highlight2 = i + 1
            colors = ["steelblue"] * len(novy_zoznam)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(novy_zoznam)), novy_zoznam, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if novy_zoznam[i] > novy_zoznam[i+1]:
                novy_zoznam[i], novy_zoznam[i+1] = novy_zoznam[i+1], novy_zoznam[i]
                zmena += 1
        if zmena == 0:
            break
    plt.ioff()
    plt.show()
    return novy_zoznam


if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    # print(small)
    # print(selection_sort(small))
    print(bubble_sort(values))