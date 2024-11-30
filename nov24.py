# At first I gave Monte Carlo simulation a go, but i couldn't get the probability to converge for the desired precision within any reasonable amount of time.

import numpy as np
from scipy.integrate import nquad

def overlap_area(r1, r2, distance):
    if distance >= r1 + r2:
        return 0.0
    elif distance <= abs(r1 - r2):
        return np.pi * min(r1, r2)**2
    else:
        part1 = r1**2 * np.arccos((distance**2 + r1**2 - r2**2) / (2 * distance * r1))
        part2 = r2**2 * np.arccos((distance**2 + r2**2 - r1**2) / (2 * distance * r2))
        part3 = 0.5 * np.sqrt((-distance + r1 + r2) * (distance + r1 - r2) * (distance - r1 + r2) * (distance + r1 + r2))
        return part1 + part2 - part3

def area_element(y_coord, x_coord):
    radius1 = np.hypot(x_coord, y_coord)
    radius2 = np.hypot(x_coord - 1, y_coord)
    sector1 = 0.25 * np.pi * radius1**2
    sector2 = 0.25 * np.pi * radius2**2
    overlap = overlap_area(radius1, radius2, 1)
    return sector1 + sector2 - overlap

def y_limits(x_coord):
    return [0, x_coord]

integral_result, _ = nquad(area_element, [y_limits, [0, 0.5]])

print(f"Probability: {integral_result * 8:.11f}")
