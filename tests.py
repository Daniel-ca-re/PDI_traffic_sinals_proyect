import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def plot_square(a, b, c, d):
    """
    Plot a square given its corner coordinates (a, b, c, d)
    """
    x = [a[0], b[0], c[0], d[0], a[0]]
    y = [a[1], b[1], c[1], d[1], a[1]]
    plt.plot(x, y, 'r-')  # 'r-' for red line
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cuadrado')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    # Initial square coordinates
    a = [0, 0]
    b = [0, 1]
    c = [1, 1]
    d = [1, 0]
    
    interact(plot_square,
             a=FloatSlider(min=-5, max=5, step=0.1, value=a[1]),
             b=FloatSlider(min=-5, max=5, step=0.1, value=b[1]),
             c=FloatSlider(min=-5, max=5, step=0.1, value=c[1]),
             d=FloatSlider(min=-5, max=5, step=0.1, value=d[1]))

if __name__ == "__main__":
    main()