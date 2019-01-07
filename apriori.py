import sys

from itertools import chain, combinations
from collections import defaultdict

def readFile(filename):
        """
        Reads each row (transaction) from the file and convert it to frozen set.
        """
        rowIterator = open(filename, 'rU')
        for transaction in rowIterator:
                frozentran = frozenset((transaction.strip().rstrip(',')).split(','))
                yield frozentran

def minimumSupportItems(repeatSet, minSupp, transactions, items):
    """
    calculates the support for items in the items and returns a subset
    of the items each of whose elements satisfies the minimum support
    filteredItem = frozenset({'apple'}), frozenset({'milk'}), frozenset({'eggs'})
    """
    minSupport = float(minSupp)
    filteredItem = set()
    temp = defaultdict(int)

    for transaction in transactions:
            for item in items:
                    if item.issubset(transaction):
                            repeatSet[item] += 1
                            temp[item] += 1

    for item, count in temp.items():
            if (float(count)/len(transactions)) >= minSupp:
                    filteredItem.add(item)
    return filteredItem

def joinSet(itemSet, length):
        """
        Return all the combinations of n(length) items in itemSet
        """
        newSet = set()
        for item in itemSet:
            for anotherItem in itemSet:
                if len(item.union(anotherItem)) == length:
                    newSet.add(item.union(anotherItem))
        return newSet

def Apriori(minConfi, minSupp):

    """
    Necessary variable declaration
    """
    transactions = list()
    items = set()
    repeatSet = defaultdict(int)
    combineSet = dict()
    finalItemSet = []
    associationRules = []

    minConfi = float(minConfi)
    minSupp = float(minSupp)

    dataset = readFile("dataset/store_data.csv")

    """
    Separate all the uniques item into items set and all transactions into transactions list
    transaction = frozenset({'apple', 'milk', 'eggs'})
    items = frozenset({'apple'}), frozenset({'milk'}), frozenset({'eggs'})
    """
    for data in dataset:
        transaction = frozenset(data)
        transactions.append(transaction)
        for item in transaction:
            items.add(frozenset([item]))

    """
    Find support for each item in dataset and filter out the items which has support higher than or equal to minimum support
    """
    itemSet = minimumSupportItems(repeatSet, minSupp, transactions, items)

    """
    Find all the combinations of item whose support is greater than minimum support and find confidence of itemset whose confidence
    is greater than minimum Confidence

    combineSet = {1: { frozenset({'apple'}), frozenset({'milk'}) }, 2: { frozenset({'apple', 'milk'}) } }
    finalItemSet = [(frozenset({'apple'}), 0.084), (frozenset({'milk'}), 0.064), (frozenset({'apple', 'milk'}), 0.043)]
    associationRules = [((('apple',), ('milk',)), 0.2641509433962264), ((('milk',), ('eggs',)), 0.31818181818181823)]
    """
    i = 2
    while(itemSet != set([])):
        for item in itemSet:
            finalItemSet.extend([((item), (float(repeatSet[item])/len(transactions)))])
            if len(item) > 1:
                for element in item:
                    element = frozenset([element])
                    confidence = (float(repeatSet[item])/len(transactions))/(float(repeatSet[element])/len(transactions))
                    if confidence >= minConfi:
                        associationRules.append(((tuple(element), tuple(item.difference(element))),confidence))

        itemSet = minimumSupportItems(repeatSet, minSupp, transactions, (joinSet(itemSet, i)))
        i = i + 1

    """
    Sorting the output in decreasing order of support and Confidence
    """
    finalItemSet = sorted(finalItemSet, key=lambda kv: kv[1], reverse=True)
    associationRules = sorted(associationRules, key=lambda kv: kv[1], reverse=True)

    return finalItemSet, associationRules
