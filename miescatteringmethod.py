# -*- coding: utf-8 -*-
"""MieScatteringMethod.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b5bZlFrx-YWPdFZdTjNLYqFRm8D1a-Vz
"""

# this model is a good one but complicated to use; I rather use Rayleigh approximation, 
# which assumes that the roughness of the surface is much smaller than the wavelength of the incident light. 
# This approximation is often used to model the scattering of light from smooth surfaces and can provide an 
# estimate of the scattered light intensity.

# I used a website to plot refarctive indeces: https://refractiveindex.info/?shelf=3d&book=metals&page=aluminium

from google.colab import files
import matplotlib.pyplot as plt
import pandas as pd
#uploaded = files.upload()

# Load the .csv files into Pandas DataFrames
df1 = pd.read_csv("RefractiveIndex_Al.csv")
df2 = pd.read_csv("RefractiveIndex_Ti.csv")
df3 = pd.read_csv("RefractiveIndex_Cu.csv")

# Rename the columns to 'wavelength' and 'n'
df1.rename(columns={df1.columns[0]: "wavelength", df1.columns[1]: "n"}, inplace=True)
df2.rename(columns={df2.columns[0]: "wavelength", df2.columns[1]: "n"}, inplace=True)
df3.rename(columns={df3.columns[0]: "wavelength", df3.columns[1]: "n"}, inplace=True)

# Plot the DataFrames
fig, axs = plt.subplots(1, 3, figsize=(12, 3))

axs[0].plot(df1['wavelength'], df1['n'], '-', label='Refractive Index Al', color='blue')
axs[0].legend()
axs[0].set_xlim([0.403, 0.780])
axs[0].set_ylim([0.45, 2.5])
axs[0].set_xlabel('Wavelength ($\mu$m)')
axs[0].set_ylabel('Refractive Index (n)')

axs[1].plot(df2['wavelength'], df2['n'], '-', label='Refractive Index Ti', color='red')
axs[1].legend()
axs[1].set_xlim([0.403, 0.780])
axs[1].set_ylim([2, 3.2])
axs[1].set_xlabel('Wavelength ($\mu$m)')
axs[1].set_ylabel('Refractive Index (n)')

axs[2].plot(df3['wavelength'], df3['n'], '-', label='Refractive Index Cu', color='orange')
axs[2].legend()
axs[2].set_xlim([0.403, 0.780])
axs[2].set_ylim([0, 2])
axs[2].set_xlabel('Wavelength ($\mu$m)')
axs[2].set_ylabel('Refractive Index (n)')

plt.tight_layout()
plt.show()

# I used this to fit a function 

from scipy.optimize import curve_fit
import numpy as np

# Define the function to be fitted
def fit_function(x, a, b, c):
    return a + b * x + c * x**2

# Get the data to be fitted
wavelength_al = df1[(df1['wavelength'] >= 0.403) & (df1['wavelength'] <= 0.780)]['wavelength'].to_numpy()
n_al = df1[(df1['wavelength'] >= 0.403) & (df1['wavelength'] <= 0.780)]['n'].to_numpy()
wavelength_ti = df2[(df2['wavelength'] >= 0.403) & (df2['wavelength'] <= 0.780)]['wavelength'].to_numpy()
n_ti = df2[(df2['wavelength'] >= 0.403) & (df2['wavelength'] <= 0.780)]['n'].to_numpy()
wavelength_cu = df3[(df3['wavelength'] >= 0.403) & (df3['wavelength'] <= 0.780)]['wavelength'].to_numpy()
n_cu = df3[(df3['wavelength'] >= 0.403) & (df3['wavelength'] <= 0.780)]['n'].to_numpy()

# Fit the data
popt_al, _ = curve_fit(fit_function, wavelength_al, n_al)
popt_ti, _ = curve_fit(fit_function, wavelength_ti, n_ti)
popt_cu, _ = curve_fit(fit_function, wavelength_cu, n_cu)

# Print the fitted function for Aluminum
print(f'Fitted function for Aluminum: n(x) = {popt_al[0]:.2f} + {popt_al[1]:.2f} * x + {popt_al[2]:.2f} * x^2')

# Print the fitted function for Titanium
print(f'Fitted function for Titanium: n(x) = {popt_ti[0]:.2f} + {popt_ti[1]:.2f} * x + {popt_ti[2]:.2f} * x^2')

# Print the fitted function for Titanium
print(f'Fitted function for Copper: n(x) = {popt_cu[0]:.2f} + {popt_cu[1]:.2f} * x + {popt_cu[2]:.2f} * x^2')

import numpy as np
import matplotlib.pyplot as plt

def scattered_intensity(wavelength, particle_size, refractive_index, incident_angle):
    """
    A simplified version of scattered intensity calculation

    Parameters:
    wavelength (float): Wavelength of the incident laser in nanometers
    particle_size (float): Particle size in microns
    refractive_index (float): Refractive index of the particle material
    incident_angle (float): Incident angle in degrees

    Returns:
    float: Scattered intensity
    """
    k = 2 * np.pi / wavelength
    size_parameter = k * particle_size
    scattered_intensity = (size_parameter**2 * (refractive_index**2 - 1)**2) / (2 * np.cos(incident_angle))
    return scattered_intensity

# Set the parameters
particle_size = 0.3 # micron
incident_angle = np.deg2rad(45)
wavelengths = np.linspace(403, 780, 378) * 1e-3 # convert to micrometers

refractive_index_Al = 1.70 - 6.88 * wavelengths + 9.93 * wavelengths**2
refractive_index_Ti = 0.84 + 3.61 * wavelengths - 1.02 * wavelengths**2
refractive_index_Cu = 6.04 - 14.88 * wavelengths + 9.36 * wavelengths**2

scattered_intensities_Al = scattered_intensity(wavelengths, particle_size, refractive_index_Al, incident_angle)
scattered_intensities_Ti = scattered_intensity(wavelengths, particle_size, refractive_index_Ti, incident_angle)
scattered_intensities_Cu = scattered_intensity(wavelengths, particle_size, refractive_index_Cu, incident_angle)

# Plot the results
plt.figure(figsize=(12,4))

plt.subplot(1, 2, 1)
plt.plot(wavelengths * 1e3, scattered_intensities_Al, label="Aluminum", color='blue')
plt.plot(wavelengths * 1e3, scattered_intensities_Ti, label="Titanium", color='red',)
plt.plot(wavelengths * 1e3, scattered_intensities_Cu, label="Copper", color='orange')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Scattered Intensity (a.u.)")
plt.title("Mie scattering for Al, Ti and Cu")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(wavelengths * 1e3, scattered_intensities_Al, label="Aluminum", color='blue')
plt.plot(wavelengths * 1e3, scattered_intensities_Ti, label="Titanium", color='red',)
plt.plot(wavelengths * 1e3, scattered_intensities_Cu, label="Copper", color='orange')
plt.xlim(403, 700)
plt.ylim(0, 30)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Scattered Intensity (a.u.)")
plt.title("Mie scattering for Al, Ti and Cu")
plt.legend()

plt.tight_layout()
plt.show()