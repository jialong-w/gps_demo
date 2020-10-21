"""Main module."""
import gps_api

port = "/dev/ttyAMA0"
gps = gps_api.GPS(port)
print(gps.get_distance(-33.9523601, 18.4590805))
# print(gps_api.__version__)
