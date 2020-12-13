import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np

### ANIMACION SIMPLE DEL SENO ###

### GENERAMOS LOS ARREGLOS DE TIEMPO Y POSICION ###
t = np.linspace(0,2*np.pi)
x = np.sin(t)

### CREAMOS LA GRAFICA DONDE TRABAJAREMOS
fig, ax = plt.subplots()
### AGREGAMOS EN AL GRAFICA UNA LINEA QUE REPRESENTA EL SENO
l, = ax.plot([0,2*np.pi],[-1,1])
### CREAMOS LA FUNCION PARA LOS FRAMES
animate = lambda i: l.set_data(t[:i], x[:i])
### GENERAMOS LA ANIMACION
ani = matplotlib.animation.FuncAnimation(fig, animate, frames=len(t))
plt.show()