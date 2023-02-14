#Compute Curl of a vector field.
import numpy as np

def curl(F, x, y, z):
    dFdx = np.gradient(F[0], x)
    dFdy = np.gradient(F[1], y)
    dFdz = np.gradient(F[2], z)
    
    curl_x = np.gradient(dFdz[1] - dFdy[2], y, z)
    curl_y = np.gradient(dFdx[2] - dFdz[0], z, x)
    curl_z = np.gradient(dFdy[0] - dFdx[1], x, y)
    
    return curl_x, curl_y, curl_z
