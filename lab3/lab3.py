import numpy as np
import matplotlib.pyplot as plt

def normalized_shifted_correlation(a, b):
    cormas = []
    maxsdvig = 0
    maxznach = np.dot(a, b)
    cormas.append(maxznach)

    for shift in range(1, len(a)):
        b = np.roll(b, 1)  # Сдвигаем вектор b на одно значение
        corab = np.dot(a, b)
        if corab > maxznach:
            maxznach = corab
            maxsdvig = shift
        cormas.append(corab)

    # Нормализация корреляции
    multa = np.dot(a, a)
    multb = np.dot(b, b)
    norm_corr = maxznach / np.sqrt(multa * multb)

    return norm_corr, maxsdvig, cormas

# Пример использования функции
a = np.array([0.3, 0.2, -0.1, 4.2, -2, 1.5, 0])
b = np.array([0.3, 4, -2.2, 1.6, 0.1, 0.1, 0.2])

norm_corr, maxsdvig, cormas = normalized_shifted_correlation(a, b)

print("Нормализованная корреляция:", norm_corr)
print("Максимальная корреляция:", maxsdvig)

# Построение графиков
plt.figure(figsize=(10, 10))

plt.subplot(5, 1, 1)
plt.plot(a)
plt.title("a = [0.3 0.2 -0.1 4.2 -2 1.5 0]")

plt.subplot(5, 1, 2)
plt.plot(b)
plt.title("b = [0.3 4 -2.2 1.6 0.1 0.1 0.2]")

plt.subplot(5, 1, 3)
plt.plot(np.arange(len(b)), np.roll(b, maxsdvig))
plt.title("b со сдвигом")

plt.subplot(5, 1, 4)
plt.plot(cormas)
plt.title("Корреляция со сдвигом b")

# Нормализованная корреляция со сдвигом
plt.subplot(5, 1, 5)
plt.plot(cormas / np.sqrt(np.dot(a, a) * np.dot(b, b)))
plt.title("Нормализованная корреляция со сдвигом b")

plt.tight_layout()
plt.show()
