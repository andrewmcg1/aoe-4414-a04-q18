# script_name.py
#
# Usage: python3 eci_to_ecef.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Andrew McGrellis
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv
import numpy as np

# "constants"
R_E_KM  = 6378.1363
EE_E    = 0.081819221456
W       = 7.292115e-5

# helper functions


## function description
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
if len(sys.argv) == 10:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    eci_x_km = float(sys.argv[7])
    eci_y_km = float(sys.argv[8])
    eci_z_km = float(sys.argv[9])
else:
  print(\
   'Usage: '\
   'python3 arg1 arg2 ...'\
  )
  exit()

# write script below this line

julian_date = day - 32075 + int((1461 * (year + 4800 + int((month - 14) / 12))) / 4) + int((367 * (month - 2 - 12 * int((month - 14) / 12))) / 12) - int((3 * int((year + 4900 + int((month - 14) / 12)) / 100)) / 4)
julian_midnight = julian_date - 0.5
date_fractional = (second + 60 * (minute + 60 * hour)) / 86400
julian_date_fractional = julian_midnight + date_fractional

t_ut1 = (julian_date_fractional - 2451545.0) / 36525

gmst_angle = 67310.54841 + (876600 * 60 * 60 + 8640184.812866)*t_ut1 + 0.093104*t_ut1**2 - 6.2e-6*t_ut1**3
gmst_angle_radians = math.radians((gmst_angle / 240)) % (2*math.pi)

print(gmst_angle_radians)