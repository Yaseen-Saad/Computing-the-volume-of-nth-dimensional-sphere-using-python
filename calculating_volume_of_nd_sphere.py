import numpy as np
from tqdm import tqdm
import math

def gamma_function(n):
    return math.factorial(int(n-1))

total_points = 10000000
n=10
real_volume = np.pi**(n/2)/gamma_function(n/2+1)
hits = 0

def random_points(n):
    return np.random.uniform(-1,1,n)

def does_hit(points):
    if (np.sum(points**2) <=1):
        return True
    else:
        return False
    
for itteration in tqdm(range(1, total_points), desc=f"Throwing the rocks", leave=False):
    if (does_hit(random_points(n))):
        hits += 1
estimated_volume = hits/total_points*2**n
print(f"The Estimated Volume is :{estimated_volume}, whule the theoratical volume is {real_volume}, having an error of {abs(estimated_volume- real_volume)}")