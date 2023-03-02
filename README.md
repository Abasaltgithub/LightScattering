# LightScattering
This code consists of two parts. The first part fits a function to the refractive index data of three different metals, aluminum, titanium, and copper. It uses the SciPy library's curve_fit function to fit a quadratic function to each set of data. The fitted function coefficients are then printed for each metal.
The second part calculates and plots the Mie scattering for the three metals as a function of wavelength using the refractive index calculated in the previous part. The scattered_intensity function is used to calculate the scattered intensity for each metal, and the results are plotted using Matplotlib. The resulting plot consists of two subplots: the first shows the full range of wavelengths, and the second shows a limited range of wavelengths.

![Unknown-14](https://user-images.githubusercontent.com/83898640/222331965-0814f4a2-6e73-4b3f-a1bc-eb28ee1690f3.png)
![Unknown-15](https://user-images.githubusercontent.com/83898640/222331971-588ec947-96f3-4e5a-9d9e-35711f401343.png)
