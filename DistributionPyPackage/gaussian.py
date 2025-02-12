import math
import matplotlib.pyplot as plt
from .generalDistribution import Distribution

class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu = 0, sigma = 1):
        
        Distribution.__init__(self,mu,sigma)

    def read_data_file(self, file_name, sample = True):
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    
    def calculate_mean(self):
    
        """Method to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
            
        sum = 0
        for i in self.data:
            sum+=i
        self.mean = (sum/len(self.data))
        return self.mean
                


    def calculate_stdev(self, sample=True):

        """Method to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """

        if sample == True:
            n = len(self.data) - 1
        else:
            n = len(self.data)
        
        mean = self.mean#unless calculate_mean has been run before this, number will be defult. Potentially make it run before this line if not in main body

        sigma = 0
        for i in self.data:
            sigma+=((i-mean)**2)

        variance = sigma/n #no need for -1 as have done this in first 4 lines of method

        std_dev = math.sqrt(variance)

        self.stdev = std_dev

        return self.stdev

        
    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        
        plt.hist(self.data,bins=20,edgecolor='black')#bins is number of intervals
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of Data')
        plt.show()
                
        
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        first_part = 1/(math.sqrt(2*math.pi*(self.stdev**2)))       
        exponent = ((x-self.mean)**2)/(2*(self.stdev)**2)
        final_answer = first_part*10**exponent
        return final_answer

    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
    
    def __add__(self, other):
        
        """Magic method to add together two Gaussian distributions
        
        Args:
            other (Gaussian): Gaussian instance
            
        Returns:
            Gaussian: Gaussian distribution
            
        """
        
        result = Gaussian()
        
        result.mean = self.mean + other.mean #finding the mean for the sum of 2 Gaussian distributions is completed from adding them together
        result.stdev = math.sqrt((self.stdev**2)+(other.stdev**2)) #finding the std deviation for the sum of 2 Gaussian distributions is completed from squaring them and adding them to find the new variance then rooting them for the std deviation
        
        return result

    def __repr__(self):
    
        """Magic method to output the characteristics of the Gaussian instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        return "mean "+str(self.mean)+", standard deviation "+str(self.stdev)
