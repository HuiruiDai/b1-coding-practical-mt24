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
        
    def compute_action(self, reference: float, output: float) -> float:
        """
        Compute the control action based on the PD control law.
        
        :param reference: The desired reference (setpoint) at time t (r[t])
        :param output: The current system output (depth) at time t (y[t])
        :return: Control action u[t] at time t
        """
        error = reference - output  # e[t] = r[t] - y[t]
        derivative = error - self.previous_error  # find derivative based on difference between e[t] and e[t-1]

        # PD control law
        control_action = self.kp * error + self.kd * derivative
        
        # Update previous error for the next time step
        self.previous_error = error

        # return calculated control action for current time step
        return control_action