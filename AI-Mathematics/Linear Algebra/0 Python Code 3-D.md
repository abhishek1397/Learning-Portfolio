```python
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

@interact(
    a1=(-5,5,1), b1=(-5,5,1), c1=(-5,5,1), d1=(-10,10,1),
    a2=(-5,5,1), b2=(-5,5,1), c2=(-5,5,1), d2=(-10,10,1),
    a3=(-5,5,1), b3=(-5,5,1), c3=(-5,5,1), d3=(-10,10,1)
)
def plot_planes(
    a1=1, b1=1, c1=1, d1=6,
    a2=2, b2=-1, c2=1, d2=3,
    a3=1, b3=2, c3=-1, d3=4
):

    # Avoid division by zero when solving for z
    if c1 == 0 or c2 == 0 or c3 == 0:
        print("Choose non-zero values for c1, c2, and c3")
        return

    # Create grid
    x = np.linspace(-10, 10, 30)
    y = np.linspace(-10, 10, 30)
    X, Y = np.meshgrid(x, y)

    # Plane equations
    Z1 = (d1 - a1*X - b1*Y) / c1
    Z2 = (d2 - a2*X - b2*Y) / c2
    Z3 = (d3 - a3*X - b3*Y) / c3

    # Create figure
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot planes
    ax.plot_surface(X, Y, Z1, alpha=0.5, color='blue')
    ax.plot_surface(X, Y, Z2, alpha=0.5, color='red')
    ax.plot_surface(X, Y, Z3, alpha=0.5, color='green')

    # Solve system for intersection point
    A = np.array([
        [a1, b1, c1],
        [a2, b2, c2],
        [a3, b3, c3]
    ], dtype=float)

    D = np.array([d1, d2, d3], dtype=float)

    try:
        x0, y0, z0 = np.linalg.solve(A, D)

        # Highlight intersection point
        ax.scatter(
            x0, y0, z0,
            color='black',
            s=200,
            marker='o',
            label='Intersection'
        )

        # Label coordinates
        ax.text(
            x0, y0, z0,
            f'({x0:.2f}, {y0:.2f}, {z0:.2f})',
            color='black'
        )

        ax.set_title(
            f'Intersection: ({x0:.2f}, {y0:.2f}, {z0:.2f})'
        )

    except np.linalg.LinAlgError:
        ax.set_title("No unique intersection point")

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_zlim(-10, 10)

    ax.legend()
    plt.show()
```
