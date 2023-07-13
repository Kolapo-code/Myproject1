#!/usr/bin/env python3

class Distribution:
    def __init__(self, mu=0, sigma=1):
        """Generic distribution class for calculating and visualizing a probability distribution."""
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name):
        """Function to read in data from a txt file."""
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(float(line))
                line = file.readline()
        file.close()
        self.data = data_list

