ThermCoeff - Thermoelastic coefficent evaluation
------------------------------------

Thermoelastic coefficent evaluation for Thermoelastic Stress Analysis (TSA)


Simple examples
---------------

Here is a simple example on how to use the code:

.. code-block:: python

	import numpy as np
	import pyLIA
	import pysfmov as sfmov
	import ThermCoeff as km
	
Thermoelastic coefficient of standard materials is available as:

.. code-block:: python

	s = 'steel'                         # Steel material is chosen
	therm_coeff = km.from_material('s') # Thermoelastic coefficient of steel is obtained

If strain gauge calibration is performed and the strain is acquired externally during the experiment:

.. code-block:: python
	
	# Uniaxial strain-gauge					
	eps = np.random.rand(1000)		# Simulated strain from strain-gauge
	strain = km.get_strain(eps)		# Obtain strain
	
	# Strain-gauge rosette
	eps = np.random.rand(1000, 3)				# Simulated strain from rosette
	configuration = '90' 					# Angular configuration of the rosette
	strain = km.get_strain(eps, configuration)		# Obtain strain
	
Once the strain is obtained (or already known):

.. code-block:: python

	filename = './data/rec.sfmov'   # Path to the thermal video
	data = sfmov.get_data(filename) # Load the data
	fs = 400			# Sampling frequency [Hz]
	fl = 40				# Load frequency [Hz]
	location = 56, 38, 30, 70	# Location of the strain-gauge on the camera field of view

	E = 75 * 10**9 			# Young Modulus [Pa]
	ni = 0.33 			# Poisson's ratio
	
	therm_coeff = km.from_strain_gauge(data, fs, fl, E, ni, strain, location)


Reference:
<https://www.sciencedirect.com/science/article/pii/S0142112320301924>
