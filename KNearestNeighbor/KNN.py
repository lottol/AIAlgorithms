from random import shuffle
import csv
import math
import operator

"""
This will be an example of K Nearest Neighbor to classify data pulled from kaggle.com
Data set: https://www.kaggle.com/uciml/iris
I will be printing out the accuracy
Note: K must be an odd number
Assumes that the first column is an id value (and thus ignored) and that the last value is the correct classification
"""


def calculate_distance(example, target):
    """
    :param example: the given data example
    :param target:  the data point being evaluated
    :return: the distance from the point
    """
    distance = 0.0
    for i in range(1, len(example) - 1):
        distance += math.pow(float(example[i]) - float(target[i]), 2)
    distance = math.sqrt(distance)
    return distance


def knn(k, data, item):
    """
    :return: a prediction using the KNN classifier
    """
    classify = {}
    k_list = sorted(data, key=lambda x: calculate_distance(x, item))[0:k]
    for i in k_list:
        if i[len(i) - 1] in classify:
            classify[i[len(i) - 1]] += 1
        else:
            classify[i[len(i) - 1]] = 1
    return max(classify.items(), key=operator.itemgetter(1))[0]


def accuracy(k, test, train):
    """
    Calculates the percentage of correctly classified data
    """
    total = len(test)
    correct = 0
    for item in test:
        if knn(k, train, item) == item[-1]:
            correct += 1
    return correct/total


if __name__ == "__main__":
    data = []

    with open('Iris.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    category_list = data.pop(0)
    del category_list[0]
    categories = ""

    print("Classifying objects as " + category_list.pop() + " by the following categories:")
    for cat in category_list:
        categories += cat + ", "
    print(categories[:-2])

    shuffle(data)

    train = data[0:int(len(data) / 2)]
    test = data[int(len(data) / 2):len(data)]

    print("Accuracy: " + "{0:.2f}".format(accuracy(5, test, train) * 100) + "%")
