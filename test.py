import sys
sys.path.append("build")
import satellite_core

# For example, test with a TLE if you have it exposed:
tle = satellite_core.TwoLineElement(
    "1 25544U 98067A   20029.54791435  .00001264  00000-0  29620-4 0  9993",
    "2 25544  51.6434 340.5426 0007413  31.1542  51.9981 15.49121610210260"
)

position = tle.get_position()
velocity = tle.get_velocity()

print("Position (m):", position)
print("Velocity (m/s):", velocity)
