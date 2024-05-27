import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
import numpy as np


def plot_square(ang, a_x, a_y, s_x, s_y):
    """
    Plot a square given its corner coordinates (a, b, c, d)
    """



    matriz_rotacion = np.array([[np.cos(ang), -np.sin(ang)],
                                [np.sin(ang), np.cos(ang)]])
    
    # Matriz de escalado
    matriz_escala = np.array([[a_x, 0],
                               [0, a_y]])
    
    # Multiplicar las matrices de rotación y escalado
    rot = np.dot(matriz_rotacion, matriz_escala)

    sheer = np.array([[1, s_x],
                        [s_y, 1]])

    # Realizar la multiplicación de las matrices
    resultado_matriz = np.dot(sheer,rot)
    
    x = [0, 1, 0, -1, 0]
    y = [0, 1, 2, 1, 0]
    tx = [0, 0, 1, 1, 0]
    ty = [0, 1, 1, 0, 0]
    for i in range(0,len(x)):
        vector = np.array([x[i], y[i]])

        # Multiplicar el vector por la matriz resultante
        resultado_vector = np.dot(resultado_matriz, vector)
        tx[i]=resultado_vector[0]
        ty[i]=resultado_vector[1]

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, 'r-', label='Cuadrado original')
    plt.plot(tx, ty, 'b-', label='Cuadrado transformado')

    # Establecer los límites de los ejes para que siempre sea un cuadrado
    plt.xlim(-6, 6)
    plt.ylim(-6, 6)

    # Etiquetas y leyenda
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Rotación con escalado')
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

def main():
    interact(plot_square,
             ang=FloatSlider(min=-np.pi, max=np.pi, step=0.01, value=0),
             a_x=FloatSlider(min=0, max=5, step=0.01, value=1),
             a_y=FloatSlider(min=0, max=5, step=0.01, value=1),
             s_x=FloatSlider(min=-1, max=1, step=0.01, value=0),
             s_y=FloatSlider(min=-1, max=1, step=0.01, value=0))

if __name__ == "__main__":
    main()
