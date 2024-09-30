import matplotlib.pyplot as plt
import numpy as np


def err_x(self , sun_center):
        error_x = sun_center[0] - self.frameCenter[1]
        return error_x 
    
def err_y(self , sun_center):
        error_y = sun_center[1] - self.frameCenter[1]
        return error_y