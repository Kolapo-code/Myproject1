#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
from distributions.Generaldistribution import Distribution

class Gaussian(Distribution):
    """Gaussian distribution class for calculating and visualizing a Gaussian distribution."""
    
    def __init__(self, mu=0, sigma=1):
        Distribution.__init__(self, mu, sigma)
    
    def calculate_mean(self):
        """Function to calculate the mean of the data set."""
        avg = 1.0 * sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def calculate_stdev(self, sample=True):
        """Function to calculate the standard deviation of the data set."""
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
        mean = self.mean
        sigma = 0
        for d in self.data:
            sigma += (d - mean) ** 2
        sigma = math.sqrt(sigma / n)
        self.stdev = sigma
        return self.stdev

    def read_data_file(self, file_name, sample=True):
        """Function to read in data from a txt file."""
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

    def plot_histogram(self):
        """Function to output a histogram of the data."""
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('Data')
        plt.ylabel('Count')
        plt.show()

    def pdf(self, x):
        """Probability density function calculator for the Gaussian distribution."""
        return (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(
            -0.5 * ((x - self.mean) / self.stdev) ** 2
        )

    def plot_histogram_pdf(self, n_spaces=50):
        """Function to plot the normalized histogram of the data and the probability density function."""
        min_range = min(self.data)
        max_range = max(self.data)
        interval = 1.0 * (max_range - min_range) / n_spaces
        x = []
        y = []
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=0.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')
        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution')
        axes[1].set_ylabel('Density')
        plt.show()

    def __add__(self, other):
        """Function to add together two Gaussian distributions."""
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        return result

    def __repr__(self):
        """Function to output the characteristics of the Gaussian instance."""
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)

