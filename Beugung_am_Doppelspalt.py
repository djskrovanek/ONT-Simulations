# Written by David Skrovanek; Dec. 21, 2019
from numpy import pi, sin, cos
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


def interference(distance, angle, wavelength):
    """
    Interference term within intensity function
    :param distance: separation between the two slits in mm (10^3)
    :param angle: angles over which the light will travel in radians
    :param wavelength: wavelength of the incoming light in nm (10^9)
    :return interference_factor:
    """
    beta = (pi * distance * 10 ** -3 * sin(angle)) / (wavelength * 10 ** -9)
    interference_factor = (cos(beta) ** 2)
    return interference_factor


def diffraction(slit_width, angle, wavelength):
    """
    Diffraction term within intensity function
    :param slit_width:
    :param angle: angles over which the light will travel in radians
    :param wavelength: wavelength of the incoming light in nm (10^9)
    :return diffraction_factor:
    """
    alpha = (pi * slit_width * 10 ** -6 * sin(angle)) / (wavelength * 10 ** -9)
    diffraction_factor = ((sin(alpha) / alpha) ** 2)
    return diffraction_factor


def intensity_pattern(distance, wavelength, slit_width):
    """
    Intensity of the light pattern emerging on the screen
    :param distance:
    :param wavelength:
    :param slit_width:
    :return:
    """
    inter = interference(distance, theta, wavelength)
    diff = diffraction(slit_width, theta, wavelength)
    intensity = inter * diff
    return intensity


# Initializing the plot
fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(left=0.25, bottom=0.25)

# Creating initial conditions
s = 0.5  # Separation between slit and screen (in m)
theta_max = np.float64(pi / 30)
theta = np.arange(s * np.math.tan(-theta_max), s *
                  np.math.tan(theta_max), 10 ** -5)  # Range of angles over which the light will travel
d_0 = 0.155  # Initial value of separation between the two slits (in mm)
l_0 = 560  # Initial value of wavelength of incoming light (in nm)
w_0 = 25  # Initial value of slit width (in µm)

# Drawing the initial plot
[line] = ax.plot(theta, intensity_pattern(d_0, l_0, w_0), linewidth=2, color='red')
plt.title('Beugung am Doppelspalt')
plt.xlabel('Abstand zwischen Maxima [m]')
plt.ylabel('Intensität  I(θ)/I$_{0}$')
ax.set_xlim([s * np.math.tan(-theta_max), s * np.math.tan(theta_max)])
ax.set_ylim([0, 1])

# Slit separation slider
d_slider_ax = fig.add_axes([0.25, 0.13, 0.65, 0.03])
d_slider = Slider(d_slider_ax, 'Spaltmittenabstand [mm]', 0.01, 0.30, valinit=d_0)

# Wavelength slider
l_slider_ax = fig.add_axes([0.25, 0.08, 0.65, 0.03])
l_slider = Slider(l_slider_ax, 'Wellenlänge [nm]', 380, 740, valinit=l_0)

# Slit width slider
w_slider_ax = fig.add_axes([0.25, 0.03, 0.65, 0.03])
w_slider = Slider(w_slider_ax, 'Spaltbreite [µm]', 0.01, 50, valinit=w_0)


def sliders_on_changed(val):
    """
    Action for modifying the line when any slider's value changes
    :param val:
    :return:
    """
    line.set_ydata(intensity_pattern(d_slider.val, l_slider.val, w_slider.val))
    fig.canvas.draw_idle()


d_slider.on_changed(sliders_on_changed)
l_slider.on_changed(sliders_on_changed)
w_slider.on_changed(sliders_on_changed)

# Button for resetting the parameters
reset_button_ax = fig.add_axes([0.07, 0.25, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', hovercolor='0.975')


def reset_button_on_clicked(mouse_event):
    """
    Operation of reset button
    :param mouse_event:
    :return:
    """
    l_slider.reset()
    d_slider.reset()
    w_slider.reset()


reset_button.on_clicked(reset_button_on_clicked)
plt.show()
