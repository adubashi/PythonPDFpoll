# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 20:14:40 2015

@author: aduba_000
"""

import datetime
import numpy
import math

class Poll:    
    def __init__(self, title = "", description = "Dubashi Strategies" , sampleSize = 400 ,numberOfCandidates = 3 ,pollNumbers = {}
    ,studyNumber = 0, date = datetime.datetime.now(), contacts = 2000):
          self.title = title;
          self.description = description;
          self.sampleSize = sampleSize;
          self.numberOfCandidates = numberOfCandidates 
          self.pollNumbers = {};
          self.studyNumber = studyNumber;
          self.date = date;
          self.totalContacts = contacts;
          #confidence interval set at 95 percent.
          self.zvalue = 1.96
          self.marginOfError = 0;
          
    def toString(self):
        print "Company Name: " + self.companyName;
        print "Description: " + self.description;
        print "Sample Size: " + str(self.sampleSize);
        print "Number of Candidates: " + str(self.numberOfCandidates);
        print self.pollNumbers; 
        
    def addCandidate(self,candidateName = "Null Candidate",choiceList = [15,5,20]):
        self.pollNumbers[candidateName] = choiceList;
        self.calculateMarginOfError();
        
    def calculateMarginOfError(self):
        data = [];
        vals = self.pollNumbers.values();
        for i in vals:
            data.append(i[0])
        std = numpy.std(data)
        n = self.sampleSize;
        rootn = math.sqrt(n)
        self.marginOfError = self.zvalue *  (std/(rootn))
        
        
    
    
        
    
    
        

          
    