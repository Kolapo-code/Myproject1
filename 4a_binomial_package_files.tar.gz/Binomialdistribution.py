#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
from distributions.Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and visualizing a Binomial distribution. """
    
    def __init__(self, prob=.5, size=20):
        self.p = prob
        self.n = size
        self.calculate_mean()
        self.calculate_stdev()
        Distribution.__init__(self, self.mean, self.stdev)
    
    def calculate_mean(self):
        """Function to calculate the mean from p and n."""
        self.mean = self.p * self.n
        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n."""
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev
        
    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set."""
        self.n = len(self.data)
        self.p = sum(self.data) / self.n
        self.calculate_mean()
        self.calculate_stdev()
        return self.p, self.n
        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using matplotlib pyplot library."""
        plt.bar([0, 1], [self.n * (1 - self.p), self.n * self.p])
        plt.title('Bar Chart of Binomial Distribution')
        plt.xlabel('Outcome')
        plt.ylabel('Count')
        plt.show()
        
    def pdf(self, k):
        """Probability density function calculator for the binomial distribution."""
        return (
            math.comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        )
        
    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution."""
        x = list(range(self.n + 1))
        y = [self.pdf(k) for k in x]
        plt.bar(x, y)
        plt.title('Probability Density Function of Binomial Distribution')
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.show()
        return x, y
        
    def __add__(self, other):
        """Function to add together two binomial distributions with equal p."""
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise ValueError(error)
        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        return result
        
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance."""
        return f"mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}"

