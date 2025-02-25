import math
import matplotlib.pyplot as plt
import numpy as np
from generalDistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Parent Class Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
    Child Class Attributes:
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    
            
    """  
    
    def __init__(self, prob=.5, size=20):

        self.p = prob #stores the probability of a positive outcome
        self.n = size #stores size of distribution / number of total trials
        self.calculate_mean()
        self.calculate_stdev()
        Distribution.__init__(self,self.mean,self.stdev)           
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = self.p*self.n
        return self.mean



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        variance = self.n*self.p*(1-self.p)
        self.stdev = math.sqrt(variance)
        return self.stdev
        
        
        
    def replace_stats_with_data(self):#calculates p and n from dataset and updates mean and stddev from these values
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        

        #finds number of trials by seeing how many elements in list there are
        self.n = len(self.data)

        #calculates probability by finding positive outcomes and dividing them by n
        positiveCounter = 0
        for i in self.data:
            if int(i) == 1:
                positiveCounter +=1
        self.p = positiveCounter/self.n
        #now n and p have been updated we can use existing functions we defined to calculate the rest
        self.calculate_mean()
        self.calculate_stdev()
        return self.p,self.n

        
    def plot_bar(self):#plots a bar chart based comparing how many positive outcomes are in a dataset vs negative
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        # finds number of positive results from dataset
        positiveCounter = 0
        for i in self.data:
            if int(i) == 1:
                positiveCounter +=1   

        plt.bar([0,1],[len(self.data)-positiveCounter,positiveCounter])#initilises bar graph with 0 and 1 on the x axis and (total number of trials - n of positive outcomes) and (positive outcomes) as the data points
        plt.xticks(np.arange(0,2,step=1))#sets format for x axis values
        plt.xlabel('negative outcomes vs positive outcomes')
        plt.ylabel('frequency')
        plt.title('Binomial Distribution Bar graph')
        plt.show()
        
    def pdf(self, k):#calcuates the probability density function for k
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        coefficient = (math.factorial(self.n))/(math.factorial(self.n-k)*math.factorial(k))      
        equation = (self.p**k)*((1-self.p)**(self.n-k))  
        result = coefficient*equation
        return result

    def plot_bar_pdf(self):#plots a bar chart of the Probability Density Function for each value of k in a bar chart

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        pdfs = []
        k=0
        while k<self.n:
            pdfs.append(self.pdf(k))
            k+=1
        
        xAxis = []
        for i in range(len(pdfs)):
            xAxis.append(i)

        plt.bar(xAxis,pdfs)
        plt.xticks(np.arange(0,len(xAxis)+1,step=1))#sets format for x axis values
        plt.xlabel('Frequency of positive outcome')
        plt.ylabel('Probability')
        plt.title('Probability Density of each outcome in a Bar graph')
        plt.show()
                
    def __add__(self, other):#changes how the objects are processed when added together. Only completed for equal p values
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        newBinomial = Binomial()
        newBinomial.n = self.n+other.n#   The new n value is the sum of the n values of the two distributions.
        newBinomial.p = self.p#   When adding two binomial distributions of even p, the p value remains the same
        newBinomial.calculate_mean()
        newBinomial.calculate_stdev()
        return newBinomial
        
        
    def __repr__(self):#changes how the code is presented when printed
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        return "mean "+str(self.mean)+", standard deviation "+str(self.stdev)+", p "+str(self.p)+", n "+str(self.n)


# #Test input you can uncomment to view functionality

# myBinomial = Binomial()
# myBinomial.read_data_file("numbers_binomial.txt")
# myBinomial.replace_stats_with_data()
# myBinomial.plot_bar()
# myBinomial.plot_bar_pdf()
