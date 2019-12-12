from numpy import pi, sin, cos
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


def signal(d, l):
    return ((cos(pi * d * 10 ** -3 * sin(theta) / (l * 10 ** -9))) ** 2) * (
            (sin(pi * 30 * 10 ** -6 * sin(theta) / (l * 10 ** -9)) /
             (pi * 30 * 10 ** -6 * sin(theta) / (l * 10 ** -9))) ** 2)


fig = plt.figure()
ax = fig.add_subplot(111)

fig.subplots_adjust(left=0.25, bottom=0.25)

theta_max = np.float64(pi / 30)
s = 0.5  # Separation between slit and screen
theta = np.arange(s * np.math.tan(-theta_max), s * np.math.tan(theta_max), 10 ** -5)
# Range of angles over which the light will travel
d_0 = 0.155  # Initial value of separation between the two slits
l_0 = 560  # Initial value of wavelength of incoming light

# Draw the initial plot
[line] = ax.plot(theta, signal(d_0, l_0), linewidth=2, color='red')
plt.plot(theta, ((sin(pi * 30 * 10 ** -6 * sin(theta) / (l_0 * 10 ** -9)) / (
        pi * 30 * 10 ** -6 * sin(theta) / (l_0 * 10 ** -9))) ** 2),
         '--b')
plt.title('Beugung am Doppelspalt')
plt.xlabel('Abstand zwischen Maxima [m]')
plt.ylabel('Intensität  I(θ)/I$_{0}$')
ax.set_xlim([s * np.math.tan(-theta_max), s * np.math.tan(theta_max)])
ax.set_ylim([0, 1])

# Slit separation slider
d_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03])
d_slider = Slider(d_slider_ax, 'Spaltmittenabstand [µm]', 0.01, 0.30, valinit=d_0)

# Wavelength slider
l_slider_ax = fig.add_axes([0.25, 0.05, 0.65, 0.03])
l_slider = Slider(l_slider_ax, 'Wellenlänge [nm]', 380, 740, valinit=l_0)


# Action for modifying the line when any slider's value changes
def sliders_on_changed(val):
    line.set_ydata(signal(d_slider.val, l_slider.val))
    fig.canvas.draw_idle()


d_slider.on_changed(sliders_on_changed)
l_slider.on_changed(sliders_on_changed)

# Button for resetting the parameters
reset_button_ax = fig.add_axes([0.07, 0.25, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', hovercolor='0.975')


def reset_button_on_clicked(mouse_event):
    l_slider.reset()
    d_slider.reset()


reset_button.on_clicked(reset_button_on_clicked)

plt.show()
