# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 00:45:47 2015

@author: aduba_000
"""

from pdfPoll import pdfPoll


pdfPollTest = pdfPoll('bloombergPoll');
pdfPollTest.poll.title = "Dubashi Strategies Iowa Poll"
pdfPollTest.poll.studyNumber = 2145
pdfPollTest.poll.addCandidate("Steve Jobs",[5,15,20]);
pdfPollTest.poll.addCandidate("Ben Carson",[20,10,30]);
pdfPollTest.poll.addCandidate("Tom Harkin",[75,20,95]);
pdfPollTest.writeToPDF();