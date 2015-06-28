[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

# Problem

Exercise 1   In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and ? = 7.7 cm for men, and µ = 163 cm and ? = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.


# Code

## import scipy.stats

    import scipy.stats


## Get distribution with mean 178 and variance 7.7

    mu = 178
    sigma = 7.7
    dist = scipy.stats.norm(loc=mu, scale=sigma)
    
## How many people are between 5'10" and 6'1"?
    low = 70*2.54            # 5'10 feet  to cm
    high = 73 * 2.54         # 6'1 feet to cm
    
    low_range=dist.cdf(low)
    high_range=dist.cdf(high)
    covered_range=(high_range-low_range)*100
    print("People with height %s or less %s "%(low,low_range*100))
    print("People with high height or less  %s "%(high_range*100))
    print ("There are %s males from the distribution that are in the required range" %(covered_range))
    