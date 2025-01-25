# Machine_Learning
IN this repo to learn machine learning




## Decorators Explore
## Logging Explore
## Generators Explore

##  Process - 

   A process is simply an instance of a program that is being executed
   one Process cannot corrupt another process
   I/O Requirments
   Increased execution time to switch between process

## Threads
  a thread is a unit of execution within the process
  ### Single Threaded Process 
  shared code segment  , datasegment , process
  paint |--->box
        |--->circle
  ### MultiThreaded Process
  parallely shared code segment , datasegment




## Memory managment
  ### Explore tracemalloc


## Flask Framework
   1 - WSAI - web server gateway interface
   2 - Jinja 2 WEB Template Engine it combine we template with data source


   ### Basic Interface
   from flask import Flask

    '''
   it creates an instance of the Flask class.
   which will be your WSGI application.
   '''

    app = Flask(__name__)


    if __name__ == '__main__':
    app.run()




# Statistics
  ## 1 - Descripitive - 
  It consist of organising and summarizing of data (mean , median , mode)
  ## 2 - Infrential - 
  giving some information about that data (from sample data we made some assumptions based on some conclusion)
  
  ## variables
   1 - Quantitative Variable 
        a - Discrete Quantitative 
        b - countinous variable
   2 - Qualitative /Categorical 
          
 

  ## Random Variable
     Random variable is a function which  will produce value based on some experiment.
  
  ## Percentile and Quartiles
  ### Percentile -: A percentile is a value below which a certain percentage of observartion lie.
    percentile = # of values below x / x *100
   
   eg - 93 percent of entire population is below 60000
    
    
   ### Quartiles - 1/4th



   ## 5 number summary to remove outliers
   1 - Minimum
   2 - 1st Quartile
   3 - Median
   4 - 3rd Quartile
   5 - Maximum

   ## covariance and correlation
    
    ### covariance 
    - if the variables tend to increase and decrease together the co variance is positive and if one tends to increase and when other decrease the co variance is negative

    Quantify the relationship between x and y
               n       _      _
    Cov(x,y) = { (xi - x) (yi-y)/n-1
              i=1
    
     
     cov(x, x) = var(x)



 
     xi -> Datapoint of random variable x

     yi -> Sample mean of x
     _
     x  -> Datapoints of random variable y
     _ 
     y  -> sample mean of y

 The positive covariance indicates the no. of hours studied increased the exam score also.



  ** covariance does not have a specific limit value we do not say that co variance of this is greaer than this**





  ### correlation
  #### pearson correlation
  $x,y = cov(x,y)/sigmax.sigmay
  1 - The more the value towards +1 the more +ve correlated x & y
  2 -  the more the value towards -1 the more -ve correlated it is (x ,y)
  

  #### spearman rank correlation
     we  can calculate for no linear function also
      rs = cov(R(x) , R(y))/sigma(R(x))*sigma(R(y))



# Probability
 It is about determining the likelihood of an event

  
### Mutual Exclusive Event
  Two Events are Mutual Exclusiv if they cannot occur at the same time
  p(a or b) = p(a) + p(b)

### Non mutual exclusive events
   two events occur at same time
   p(a or b) = p(a) + p(b) - p(a and b)


## Multiplication Rule
   ### Independent 
       2 events are independent if they do not affect another
       Pr(H and T ) = Pr(H) * Pr(T)
   ### Dependent
       2 events are dependent if they affect another
       Pr(K and Q) = P(k)*Pr(Q/K) ---> Conditional Probability


  ## Practice Probability



  ## Probability Distribution Functions
    Probability Distribution Functions describe How the Probabilities are distributed over the random variable .

  ### 2 main of probability distribution functions 

  #### 1 - Probability Mass Function (PMF) : 
   used for discrete random variable  
   #### Cumulative Density Function: 
    ADD of probability 
    pr(X<=2) =Pr(X =1) +Pr(X=2) 
  #### 2 - Probability Density Function (PDF) : 
  used for continous random variable 
  Gradient of CDF (Cummulative Curve)
  ##### Properties of probability Density Function
  1 - Non Negativity f(x) >= 0 for all x values .
  2 - The total area under the PDF curve is equal to 1.


 With Respect to distribution F(x) function will be changed




 ## Types Of Probability Distribution
   ### Bernoulli Distribution
       The Bernoulli Distribution is the simplest discret probability distribution . It represents the probability distribution of a random variable that has exactly two possible outcomes success(with probability p) and failure (with probability 1-p) it is used to model binary outcomes such as fli or a yes/no question.
       
       Outcomes are binary

       Parameters --> 0<=p<=1
       q =1-p
       k = {0,1} => 2 outcomes

       PMF :- (p^k)*((1-p)^1-k) 
       How the data for Bernouilli Distribution
       
   ####  Explore HOw these are calculated
       Mean of Bernoulli Distribution - 
              k
       E(x) = {k.p(k)     k={0,1}
              i=0
       E(x)  = P
       

       Median of Bernoulli Distribution - 

                    0   if p<1/2 
        MEDIAN  = [0,1] if p=1/2
                    1   if p>1/2 
   
   
      Mode 
      p>q p will be the mode
          else q will be the mode 
      
      Variance
      Sigma^2 = Pr(k=0)*Pr(k=1)


  ### Bionomial Distribution
  In probability theory and statistics the binomial Distribution with parameters n and p is the discrete probability distribution of the number of successs in a sequence of n independent Experiments , each asking a yes-no question and each with its own Boolean-valued Outcome: success (with probability q = 1-p). A single success/failure experiment is also called a Bernoulli trial or Bernoulli experiment and a sequence of outcomes is called a Bernoulli process ; for a single trial , i>e., n=1 , the binomial distribution is a Bernoulli DIstribution. the  binomial distribution is the basis for popular binomial test of statistical significance.

   * Discrete Random VAriable
   * Every outcome of the experiment is binary
   * THese Experiments are performed for n trial

   Notaion for binary distribution B(n,p)
   Parameters: n E { 0 , 1 , 2 ....} => no.of tials or experiment
   p e [0,1] -> Success probability for each trial
   q = 1-p


   Support :- k E {0 ,1 ,2 ,3 ...,n} => Number of succes 
                      n   k     n-k
   PMF :- Pr(k,n,p) =  c P (1-p)
                        k
        

        Where k = 0 ,1, ,2 ,3 ...
    Mean : n.p
    Variance: n.p.q



  ### Poisson Distribution
   In Probability Theory and statistics the poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occuring in a fixed interval of time if these events occur with a known constant mean rate and independently of time since the last event 

   * Dicrete random variable 
   * Describe the number of events occuring in a fixed interval of time 
  Lamda => Expected no. of events occuring at every time interval

  PMF  -> e^-lamda * lamda^x /x! 
  

  Mean of poisson distribution 
  Mean = E(x) = u = lamda*t 
  lamda = Expected no. of events occur at every time interval
  t = Time interval 


  ### Normal / Gaussian Distribution (Important)

     In Probability theory and satistics a normal distribution or Gaussian distribution is a type of continous probability distribution for a real - valued random variable .


     * Continuos random variable  
     * Mean = median  = mode symmetric distribution
     * Notation N(u , sigma^2)
     * Parameters:- mean E Real value
     *  
     * 
     * as the variance increase spread increase


     PDF  -> (1/(sigma*(2pi)^1/2))*(e^-1/2)*((Xi - )/(sigma))^2
    
     Assumption - 
     #### Emperical Rule of normal /gaussian distribution
     X = { _ _ _ _ _ _ __ } => Normal /Gaussian Distribution
     Probability 
     Pr(mean - sigma <= X<= mean + sigma) =  68%
     Pr() = 95%
     Pr() = 

   1- Standard Normal Distribution 
      where mean  = 0 , standard deviation  = 1
    Z-score = (xi - mean)/standard deviation
    for converting gaussian distribtuion to standard normal distribution 

    
    X = {1 ,2 ,3 ,4 ,5 }
    mean = 3 
    sigma = 1.44 = 1




## Uniform Distribution

  ### Continuous uniform distribution  
    Continous random variable 
    in probability theory and statistics the continuous uniform distribution or rectangular distribution 

             1/(b-a)        xE[a,b]
    PDF =     0             otherwise





    CDF = {     0         for  x<a  
            (x-a)/(b-a)   for x E [a,b] 
                1         for x>b




mean = (1/2)(a+b)
median = (1/2)(a+b)

pr(x1<=X<=x2)= (x2-x1)/b-a 


  ### Discrete Random Variable 
   In probability theory and statistics the discrete uniform distribution is a symmetric probability distribution where in a finite number of values are equally likely to be observed ; every one of n values has equal probability 1/n.Another way of saying "discrete uniform distribution" would be a known ,finite number of outcomes equally likely to happen 
   
   PMF = 1/n

   mean = (a+b)/2


## Log Normal Distribution
(Right skewed distribution)
IN probabilty theory , a log normal distribution is a continous distribution of a random variable whoos logarithm is normally distributed .thus if the random variable X is log normally distributed ,then Y = ln(X) has a normal distribution .Equivalently , if Y has a normal distribution , then the exponential function of Y,X  = exp(Y) , has a log-normal distribution


X = lognormaldistribution(MEAN , standarddeviation)
y = ln(X) = normal distribution QQplot
x = exp(Y) => Log normally distributed 

mean is constant but  standard deviation is changing


## Power law distribution (80-20% rule)

IN statistics a power law is a functional relationship between two quantities ,where a relative change in one quantity results in a proportional relative change in the other quatity , independent of the intial size of those quantities one quantity varies as a power of another.



## Pareto Distribution(80-20% rule)

  BOx -Cox Transformation to conver pareto distribution in normal distribution


## Central Limit Theorem 
the central limit theorem reliies on the concept of a struggling distribution which is the probability distribution of a statistic for a large number of samples taken from a 
Population

THe central limit theorem says that the sampling distribution of the mean will always be normally distribution , as long as the sample lsize is large enough . Regardless of weather the population has a normal , poisson  , binomial , or an other distribution  ,the sampling distribution of the mean will be normal.


Mean of sampled data is same as older one
satndard deviation will be = sigma/(n)^(1/2)




# Infrential Statistics - to come up with conclusiona and infrences
## Estimates 
   Is specified observed numerical value used to estimate and unknown population paramenter


   1 - Point Estimate : Single numerical value used to estimate an unknown population parameter .
   eg - sample mean is a point estimate of population mean 
   2 - Interval Estimate : Range of values is used to estimate unknown population parameter. (confidence interval )

## A Hypothesis and hypothesis testing mechanism 
   Hypothesis Testing Mechanism 
   1 - Null Hypothesis(H0) 
     the assumption you are begning with
   2 - Alternate Hypothesis (H1)
     Opposite of null hypothesis
   3 - Experiments  -> Statistical Analysis
  4 Accept the Null Hypothesis


  ### P value 
  the p value is a number , calculated from a statistical test , that describe how likely you are to have found a particular set of observation if the null hypothesis were true ,P hypothesis testing to help decide whether to reject the null hypothesis.
  
  ### Significance value
      p< significance value reject the null hypothesis
    

    1 - Z test -> average  
    2 - T test -> average 
    3 - CHI square -> statistacal analysis for categorical data
    4 - Annova ->  variance



### Student t distribution
 In z stats when we perform any analysis using z -score 

 HOw do we perform any analysis when we do not know the population deviation  = > use student t distribution 

 t = x -mean /s/(n)^(1/2)    t table

 z score means how much it is away from the table 
### Degree of freedom 
  dof = n-1 
  

### T- stats :- 
 


 ## Baye's Theorem 
  Probability -> 
  Independent Events - one event does not effect other
  dependent events - Pr(R and Y) = P(R) * {p(y/r)} => conditional probability of r give y

  p(b/a) = (p(b)*p(a/b))/p(a)

  A,B = events
  p(A/B) = Probability of a given b is ture (already occurred)
  p(A) , p(B) = Independent Probability of A and B


  ## Confidence Interval and margin of error (Explore)


  ## Chi Square Test 
  the chi square test for goodness of fit test claims about population proportions
  it is a non parametric test that is performed on categories [ordinal and nominal] data.
  * Goodness of fit test  

  ## ANOVA(Analysis of variance):
  Annova is a statistical method used to compare the means of 2 or more groups.

  ANOVA : 
  1: Factors (variable) :
  2: Levels 
  Mode of payment


### Anova Assumptions
Assumtions in Anova

1 - Normalizing of sampling distribution of mean
 the distribution of sample mean is normally distributed
2 - Absence of Outliers
 Outlying score need to be removed from the dataset
 3 - Homogenity of variance
 Population variance in different levels of each independent variable are equal
 4 - Samples are independent and random selected

Types of ANOVA : 
1-One way ANOVA : One factor with atleast 2 levels these levels are independent

2 - Repeated Measures Annova :- One factor with atleast 2 levels ,levels are dependent 

3 - Factorial Anova : - Two or more factors (each of which with atleast ) 2 levels ,levels can be independent and dependent.




Hypothesis Testing In Annova(Partioning of variance in the annova)
NULL Hypothesis 
mean1 = mean2 = mean3 = .... mean k
Alternate Hypothesis H1 : Atleast One of the sample mean is not equal

Test Statistic : F = Variance Between Samples / Variance Within Samples 
variance between samples  

 If f is greater than critical value then we reject the null hypothesis
 Degree of freedom within - a-1
  Degree of freedom Between - N- a (no.of diffrent level)
   Degree of freedom total - N-1


1: SS between = { ({ai)^2/n - T^2/N 
2: SS within = {y^2 - {({ai)^2 / n
3: SS Total  = 

           SS     df     MS  = SS/df   F

Between
Within
Total     108.6