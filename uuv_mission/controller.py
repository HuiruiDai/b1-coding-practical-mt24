import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define a PD controller

class PDController:
    def __init__(self, kp: float, kd: float):
        """
        Initialize the PD controller with proportional and derivative gains and previous error e[t] for t smaller than 0.
        
        :param kp: Proportional gain (Kp)
        :param kd: Derivative gain (Kd)
        :param previous_error: e[t] = 0 for t < 0
        """
        self.kp = kp
        self.kd = kd
        self.previous_error = 0