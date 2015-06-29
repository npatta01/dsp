[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

# Problem

In Section 9.3, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.
An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Section 9.10.

Write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation.

Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?


# Code

## Class DiffMeansResample that implements resampling instead of permutation

    class DiffMeansResample(hypothesis.DiffMeansPermute):
        """Tests a difference in means using resampling."""
        
        def RunModel(self):
            """Run the model of the null hypothesis.
    
            returns: simulated data
            """
            group1 = np.random.choice(self.pool, self.n, replace=True)
            group2 = np.random.choice(self.pool, self.m, replace=True)
            return group1, group2
  
  
  
## imports     
    
    
    import first
    import hypothesis
    import scatter
    import thinkstats2
    import numpy as np
    
    
    
## data    

    live, firsts, others = first.MakeFrames()
    preglength_data = firsts.prglngth.values, others.prglngth.values
    
    # drop the weights with missing values
    
    weight_data = (firsts.totalwgt_lb.dropna().values,
                              others.totalwgt_lb.dropna().values)
    
    
## Difference between pregnancy length (resampling  model) 
    
    ht = DiffMeansResample(preglength_data)
    
    p_value = ht.PValue(iters=10000)
    print('\nmeans resampling preglength')
    print('p-value =', p_value)



means resampling preglength
p-value = 0.1675


## Difference between pregnancy length ( permutation  model)
    
    ht = hypothesis.DiffMeansPermute(preglength_data)
    
    p_value = ht.PValue(iters=10000)
    print('\nmeans permute preglength')
    print('p-value =', p_value)

means permute preglength
p-value = 0.1729
    
## Difference between weights (resmpling model)
    ht = DiffMeansResample(weight_data)
    p_value = ht.PValue(iters=10000)
    print('\nmeans resampling birthweight')
    print('p-value =', p_value)

means resampling birthweight
p-value = 0.0    
    
## Difference between weights (permutation model)

     ht = hypothesis.DiffMeansPermute(weight_data)
     p_value = ht.PValue(iters=10000)
     print('\nmeans resampling birthweight')
     print('p-value =', p_value)

 means permute birthweight
 p-value = 0.0 
 
 
 Looking at the models using permutation vs  resampling has no effect on the results