import numpy as np
from scipy import stats

class Statistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return {data_set_name: np.mean(values) for data_set_name, values in self.data.items()}

    def median(self):
        return {data_set_name: np.median(values) for data_set_name, values in self.data.items()}

    def standard_deviation(self): #ddof=1 is for reg. standard deviation, and ddof=0 is for pop. standard deviation
        return {data_set_name: round(np.std(values, ddof=0), 2) for data_set_name, values in self.data.items()}


# Example usage with multiple data sets
data_set = {
    "Data Set I": [97.3, 85.9, 118.8, 93.9, 66.6, 109.2, 64.9, 83.1, 100.6, 99.3, 94.9, 94.4, 139.3, 108.8, 158.1, 142.4, 85, 108.2, 116.3, 141.5, 51.4, 125.6, 70.6, 74.6, 69.9, 115.4, 84.6, 92, 97.2, 55.1, 126.6, 116.7, 76, 109.6, 63],
    "Data Set II": [59.9, 115.7, 126.1, 50.3, 133.1, 89.3, 82.5, 67.1, 60.7, 79.9, 50.1, 81.7, 83.9, 102.5, 109.9, 105.1, 67.9, 107.5, 54.9, 41.5, 59.5, 65.9, 76.9, 66.9, 85.9, 113.9, 70.3, 90.1, 99.7, 96.7],
    # "Data Set III": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    # "Data Set IV": [2, 4, 4, 4, 4, 4, 4, 4, 10, 10],

}

statistics = Statistics(data_set)
print("Mean: ", statistics.mean(), "\n")
print("Median: ", statistics.median(), "\n")
print("Standard Deviation: ", statistics.standard_deviation(), "\n")


class PopulationStandardDeviation:
    def __init__(self, data):
        """
        Initialize the class with a list of numbers.
        :param data: list of numerical values
        """
        self.data = data

    def mean(self):
        """
        Calculate the mean of the data.
        :return: float
        """
        return sum(self.data) / len(self.data)

    def population_variance(self):
        """
        Calculate the population variance.
        :return: float
        """
        mu = self.mean()
        return sum((x - mu) ** 2 for x in self.data) / len(self.data)

    def population_std_dev(self):
        """
        Calculate the population standard deviation.
        :return: float
        """
        return self.population_variance() ** 0.5
    

# data_poppy = {67, 72, 77, 78, 82}
# calculator = PopulationStandardDeviation(data_poppy)
# std_dev = round(calculator.population_std_dev(), 1)
# print("Population Standard Deviation is",std_dev)