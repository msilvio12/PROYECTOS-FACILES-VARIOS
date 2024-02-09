import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

def dibujar_piramide(ax, nombre, base, altura, x, y):
    x_values = np.array([x, x + base, x + base / 2, x])
    y_values = np.array([y, y, y + altura, y])

    path = Path(np.column_stack([x_values, y_values]))
    patch = PathPatch(path, facecolor="khaki", edgecolor="black")
    ax.add_patch(patch)

    ax.text(x + base / 2, y + altura / 2, nombre, ha="center", va="center", fontsize=8, color="black")

def dibujar_fondo(ax):
    cielo = PathPatch(Path([(0, 0), (0, 200), (500, 200), (500, 0), (0, 0)]), facecolor="skyblue", edgecolor="none")
    arena = PathPatch(Path([(0, 0), (0, 50), (500, 50), (500, 0), (0, 0)]), facecolor="sandybrown", edgecolor="none")
    
    ax.add_patch(cielo)
    ax.add_patch(arena)

def dibujar_sol(ax):
    ax.scatter(450, 150, s=100, color="yellow", marker="o", edgecolors="orange", linewidth=2, zorder=5)
    ax.text(450, 150, "Sol", ha="center", va="center", fontsize=10, color="black")

def dibujar_piramides():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    dibujar_fondo(ax)
    dibujar_sol(ax)

    datos_piramides = [
        {"nombre": "Keops", "base": 100, "altura": 150, "x": 50, "y": 50},
        {"nombre": "Kefrén", "base": 80, "altura": 120, "x": 200, "y": 70},
        {"nombre": "Micerinos", "base": 60, "altura": 90, "x": 350, "y": 90}
    ]

    for piramide in datos_piramides:
        dibujar_piramide(ax, **piramide)

    ax.set_xlim(0, 500)
    ax.set_ylim(0, 200)
    ax.axis('off')

    plt.show()

if __name__ == "__main__":
    dibujar_piramides()
