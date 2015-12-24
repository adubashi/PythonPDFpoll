# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:45:47 2015

@author: aduba_000
"""

from pdfPoll import pdfPoll


pdfPollTest = pdfPoll('bloombergPoll');
pdfPollTest.poll.title = "Dubashi Strategies Iowa Poll"
pdfPollTest.poll.studyNumber = 2145
pdfPollTest.poll.addCandidate("Steve Jobs",[5,75,80]);
pdfPollTest.poll.addCandidate("Ben Carson",[20,10,30]);
pdfPollTest.poll.addCandidate("Tom Harkin",[65,5,70]);
pdfPollTest.poll.addCandidate("Harry Enten",[10,10,20]);
pdfPollTest.writeToPDF();