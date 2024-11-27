import math
from scipy.stats import norm

# Variables
S = 42  # Underlying Price
K = 40  # Strike Price
T = 0.5  # Time of Expiration - 6 months
r = 0.10  # Risk-Free Rate - 10%
vol = 0.4  # Volatility

d1 = (math.log(S / K) + (r + 0.5 * vol ** 2) * T) / (vol * math.sqrt(T))

d2 = d1 - (vol * math.sqrt(T))

# Calculate call option price
C = S * norm.cdf(d1) - K * math.exp(-r*T) * norm.cdf(d2)

# Calculate put option price
P = K * math.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)


print(f"d1 Value: {round(d1, 4)}")
print(f"d2 Value: {round(d2, 4)}")
print(f"Call option Value: ${round(C, 2)}")
print(f"Put option value: ${round(P, 2)}")

"""
--NOTES--
1. The call and put option prices have the inverse effect, if the probability of a call option increases the price, the 
price of the put option will decrease because its less likely that it will be the strike price at the time of expiration
2. An increase in volatility will cause a price increase in both the call and put option
3. An increase in the time of expiration will increase the price of both the call and put option because there is a rise
in probability that the strike price at the time of expiration is in the money
"""
