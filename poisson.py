import scipy.stats as stats

days = int(input("enter expect value"))

prob1 = 1-stats.poisson.cdf(days, 15)

print(prob1)

prob2 = stats.poisson.cdf(21,15) - stats.poisson.cdf(16,15)

print(prob2)