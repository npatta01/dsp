[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Are first babies heavier or lighter than others

Cohen's d is a measure that can be used to capture the effect size; difference between two groups

Avg weight for first child is 7.20109443044 with var 2.01802730092
Avg weight for second child is 7.32585561497 with var 1.9437810259
Cohen d for weight is -0.0886729270726


Avg preg length for first child is 38.6009517335 with var 7.79471350923
Avg preg length for second child is 38.5229144667 with var 6.8426835193
Cohen d for preg length is 0.0288790446544


The difference between the weight of two groups (first child, not first child) mean is -0.088 standard deviation. The difference between the pregnancy length of two groups (first child, not first child) mean is 0.028 standard deviation.
In both the weight and pregnancy length, the difference is too small to be meaningful.

The book quoted the difference between male and female heights as 1.7 standard deviation. That is an example of an extremee effect size.

[Code](http://nbviewer.ipython.org/github/npatta01/ThinkStats2/blob/master/code/cohen.ipynb)


    def CohenEffectSize(group1, group2):
        diff = group1.mean() - group2.mean()
        var1 = group1.var()
        var2 = group2.var()
        n1, n2 = len(group1), len(group2)
        pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
        d = diff / math.sqrt(pooled_var)
        return d
        
    preg = nsfg.ReadFemPreg()
    #babies that lived
    live = preg[preg.outcome == 1]
    # first baby of mother
    firsts = live[live.birthord == 1]
    # second and later babies of mother
    others = live[live.birthord != 1]
    
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()
    
    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()
    
    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('Avg weight for first child is %s with var %s' %(mean1,var1))
    print('Avg weight for second child is %s with var %s' %(mean2,var2))
    print('Cohen d for weight is', d)
    
    mean1 = firsts.prglngth.mean()
    mean2 = others.prglngth.mean()
    
    var1 = firsts.prglngth.var()
    var2 = others.prglngth.var()
    d = thinkstats2.CohenEffectSize(firsts.prglngth, others.prglngth)
    
    print('Avg preg length for first child is %s with var %s' %(mean1,var1))
    print('Avg preg length for second child/later is %s with var %s' %(mean2,var2))
    print('Cohen d for preg length is', d)