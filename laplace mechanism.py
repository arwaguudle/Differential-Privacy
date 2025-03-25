import numpy as np
import pandas as pd

#the laplace mechanism
#using the example generated


ages = [25,30,35,40,45,50,55,60,65,70] #10 patients with the following ages

true_average_age = np.sum(ages)/len(ages)

sensitivity = (np.max(ages)-np.min(ages))/len(ages)

epsilon = 1.0 #this is given

noise_scale = sensitivity/epsilon

laplace_noise = np.random.laplace(0,noise_scale)

repeated_average_age = true_average_age + laplace_noise
print(repeated_average_age)