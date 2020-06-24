Thermoelastic coefficent evaluation
------------------------------------

Thermoelastic coefficent evaluation


Simple examples
---------------

Here is a simple example on how to use the code:

.. code-block:: python

	import numpy as np
	import pyLIA
	import pysfmov as sfmov
	import calibration

	filename = './data/rec.sfmov'   # Path of the thermal video
	data = sfmov.get_data(filename) # Load the data
	fs = 400			# Sampling frequency [Hz]
	fl = 40				# Load frequency [Hz]
	location = 56, 38, 30, 70	# Location of the strain-gauge on the camera field of view

	E = 75*10**9 			# Young Modulus [Pa]
	ni = 0.33 			# Poisson's ratio
	
If standard material from literature is used:
.. code-block:: python

	s = 'steel'                         # Steel material is chosen
	km = calibration.from_material('s') # Thermoelastic coefficient of steel is obtained

If strain :



Reference:
<https://www.sciencedirect.com/science/article/pii/S0142112320301924>
