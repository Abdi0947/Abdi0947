# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

import collections

class FrequencyTracker:
    def __init__(self):
        self.occ = collections.defaultdict(int)
        self.freq = collections.defaultdict(int)

    def add(self, number):
        self.occ[number] += 1
        f = self.occ[number]
        self.freq[f] += 1
        self.freq[f - 1] -= 1

    def deleteOne(self, number):
        if self.occ[number] > 0:
            self.occ[number] -= 1
            f = self.occ[number]
            self.freq[f] += 1
            self.freq[f + 1] -= 1

    def hasFrequency(self, frequency):
        return self.freq[frequency] > 0
