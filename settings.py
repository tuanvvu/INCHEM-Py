# -*- coding: utf-8 -*-
"""
User set variable input file for INCHEM-Py. 
A detailed description of this file can be found within the user manual.

Copyright (C) 2019-2021 
David Shaw : david.shaw@york.ac.uk
Nicola Carslaw : nicola.carslaw@york.ac.uk

All rights reserved.

This file is part of INCHEM-Py.

INCHEM-Py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

INCHEM-Py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with INCHEM-Py.  If not, see <https://www.gnu.org/licenses/>.
"""

filename = 'mcm_v331.fac' # facsimile format input filename

particles = True # Are we including particles. Boolean

INCHEM_additional = True #Set to True if additional reactions from the INCHEM are being used
#that do not appear in the MCM download

custom = False # Custom reactions that are not in the MCM included?
# Format of this file is in an included custom file called custom_input.txt.

temp = 293.         # temperature in Kelvin
rel_humidity = 50.  # relative humidity
M = 2.51e+19        # number density of air (molecule cm^-3)

# place any species you wish to remain constant in the below dictionary. Follow the format
const_dict = {
    'O2':0.2095*M,
    'N2':0.7809*M,
    'H2':550e-9*M,
    'saero':1.3e-2, #aerosol surface area concentration
    'CO':2.5e12,
    'CH4':4.685E13,
    'SO2':2.5e10}


"""
Outdoor indoor exchange
"""
AER = 0.5/3600  # Air exchange rate per second
diurnal = True     # diurnal outdoor concentrations. Boolean
city = "Bergen_urban" #source city of outdoor concentrations of O3, NO, NO2, and PM2.5
# options are "London_urban", "London_suburban" or "Bergen_urban"
# Changes to outdoor concentrations can be done in outdoor_concentrations.py
# See the INCHEM-Py manual for details of sources and fits


"""
Photolysis
"""
date = "21-06-2020"  # day of simulation in format "DD-MM-YYYY"
lat = 45.4         # Latitude of simulation location
light_type="Incand"  # Can be "Incand", "Halogen", "LED", "CFL", "UFT", "CFT", "FT", or "off"
#"off" sets all light attenuation factors to 0 and therefore no indoor lighting is present.
light_on_times=[[7,19],[31,43],[55,67],[79,91]] 
#[[light on time (hours), light off time (hours)],[light on time (hours),light_off_time (hours)],...]
glass="glass_C" # Can be "glass_C", "low_emissivity", "low_emissivity_film", or "no_sunlight".
#"no_sunlight" sets all window attenuation factors to 0 and therefore no light enters from outdoors.


"""
Surface deposition
"""
# The surface dictionary exists in surface_dictionary.py in the modules folder.
# To change any surface deposition rates of individual species, or to add species
# this file must be edited. Production rates can be added as normal reactions
# in the custom inputs file. To remove surface deposition HMIX can be set to 0.
# HMIX is the surface to volume ratio
HMIX = 0.02 #0.01776


"""
Initial concentrations in molecules/cm^3 saved in a text file
"""
initials_from_run = False
# initial gas concentrations can be taken from a previous run of the model. 
# Set initials_from_run to True if this is the case and move a previous out_data.pickle
# to the main folder and rename to in_data.pickle. The code will then take this
# file and extract the concentrations from the time point closest to t0 as 
# initial conditions.

# in_data.pickle must contain all of the species required, including particles if used.

# If initials_from_run is set to False then initial gas conditions must be available
# in the file specified by initial_conditions_gas, the inclusion of particles is optional.
initial_conditions_gas = 'initial_concentrations.txt'


"""
Timed concentrations
"""
timed_emissions = False # is there a species, or set of species that has a forced density change
# at a specific point in time during the integration? If so then this needs to be set to True
# and the dictionary called timed_inputs (below) needs to be populated

# the dictionary should be populated as
# timed_inputs = {species1:[[start time (s), end time (s), rate of increase in (mol/cm^3)/s]],
#                 species2:[[start time (s), end time (s), rate of increase in (mol/cm^3)/s]]}
timed_inputs = {"LIMONENE":[[36720,37320,5e8],[37600,38000,5e8]],
                "APINENE":[[36800,37320,5e8]]}


"""
Integration
"""
dt = 120                        # Time between outputs (s), simulation may fail if this is too large 
t0 = 0                          # time of day, in seconds from midnight, to start the simulation
seconds_to_integrate = 86400    # how long to run the model in seconds (86400*3 will run 3 days)


"""
Output
"""
# An output pickle file is automatically saved so that all data can be recovered
# at a later date for analysis. 
custom_name = "Bergen_urban"

# This function purely outputs a graph to the 
# output folder of a list of selected species and a CSV of concentrations. 
# If the species do not exist in the run then a key error will cause it to fail
output_graph = True #Boolean
output_species = ['O3',"O3OUT"]


"""
Run the simulation
"""
if __name__ == "__main__":
    from modules.inchem_main import run_inchem
    run_inchem(filename, particles, INCHEM_additional, custom, temp, rel_humidity,
               M, const_dict, AER, diurnal, city, date, lat, light_type, 
               light_on_times, glass, HMIX, initials_from_run,
               initial_conditions_gas, timed_emissions, timed_inputs, dt, t0,
               seconds_to_integrate, custom_name, output_graph, output_species)