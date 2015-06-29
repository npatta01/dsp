# Learn Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats" width="250" style="float: left;" />](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.


Complete the following exercises. They come from Think Stats, and some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (Cohen's d)
2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (a random distribution)
4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (blue men)
5. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (household income)
6. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (weight vs. age)
7. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
8. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
9. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)


---

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin?
------

Bayes rule


P(A|B)  => P(B|A)P(A) / P(B)        
        => P(B|A)P(A) / ( P(B|A)P(A) + P(B|A')P(A') )
       
        
A = probability of identical twins
B =  twin boy (identical or fraternal)        

P(fraternal twin) = 1/125
P(identical twin) = 1/300

Note: identical twins are of  the same sex


P(A|B)  = P(identical twins | twin brother)

P(identical twins and twin brother) = P(boys |identical twins) P (identical twins)
                                    = 1/2 * 1/300
                                    
identical twins can be Boy,Boy or Girl,Girl.... so two options

P(fraternal twins and twin brother) = P(boys | fraternal twins) P ( fraternal twins)
                                    = 1/4 * 1/125
                                    
 Fraternal twins possibilities: BB BG GG GB
   So Boy,Boy is 1/4
   
   
P(identical twins | twin brother) = 
    P(identical twins and twin brother) / 
        P (identical twins and twin brother) +P (fraternal twins and twin brother)  

= (1/2 * 1/300 ) /  ( (1/2 * 1/300 )  + ( 1/4 * 1/125) )

= 0.45

---


How do frequentist and Bayesian statistics compare?
---

They differe in how they treat the hypothesis and data.
Frequentis focus on  probability of seeing a data given a hypothesis. P(Data|hypothesis)

Bayesians focus on probability of seeing a hypothesis given a data... P(hypothesis | data)

In the bayes model, the data is considered fixed and hypotheses are random.

In the frequnetis model, the hypothesis is fixed and treats data as repeatabel random sample


[Reference] (https://oikosjournal.wordpress.com/2011/10/11/frequentist-vs-bayesian-statistics-resources-to-help-you-choose/)