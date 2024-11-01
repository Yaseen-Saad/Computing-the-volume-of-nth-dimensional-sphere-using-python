# Estimating the Volume of an n-Dimensional Hypersphere Using a Monte Carlo Simulation

This project uses a Monte Carlo simulation to estimate the volume of an \( n \)-dimensional hypersphere (or \( n \)-sphere) of unit radius. By generating random points in an \( n \)-dimensional hypercube and determining the proportion that fall within the hypersphere, we can approximate the hypersphere's volume.

## Theory and Derivation

### Hypersphere Volume Formula

The volume \( V_n \) of an \( n \)-dimensional hypersphere with radius \( r = 1 \) can be expressed as:

\begin{equation}
V_n = \frac{\pi^{n/2}}{\Gamma\left(\frac{n}{2} + 1\right)}
\end{equation}

where \( \Gamma \) is the gamma function, a generalization of the factorial function that satisfies:
- \( \Gamma(n) = (n - 1)! \) for positive integers \( n \).
- For half-integers and other real values, \( \Gamma \) can be calculated using integral definitions or approximations.

### Monte Carlo Estimation of Volume

To estimate the volume, we employ the following steps:

1. **Enclose the Hypersphere in an n-Dimensional Hypercube**:  
   A hypersphere with radius \( r = 1 \) fits within a hypercube of side length \( 2 \) and volume \( 2^n \).

2. **Generate Random Points**:  
   Random points are generated uniformly within the hypercube.

3. **Check Points for Inclusion in the Hypersphere**:  
   For a point \( (x_1, x_2, ..., x_n) \) in \( n \)-dimensional space, if 

   \[
   x_1^2 + x_2^2 + ... + x_n^2 \leq 1
   \]

   the point lies within the hypersphere.

4. **Estimate Volume**:
   By calculating the ratio of points that fall inside the hypersphere to the total points generated, we estimate the hypersphere volume as:

   \[
   V_n \approx \frac{\text{Number of points inside hypersphere}}{\text{Total number of points}} \times 2^n
   \]

### Hypothesis

The Monte Carlo estimation should yield an approximate value close to the theoretical volume derived from the formula above. By increasing the number of random points (total samples), we expect the estimated volume to converge toward the theoretical value, reducing the error.
