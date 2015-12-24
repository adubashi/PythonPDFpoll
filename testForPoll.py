# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:41:07 2015

@author: aduba_000
"""

from Poll import Poll


poll = Poll();



poll.addCandidate("Steve",[10,10,20])
poll.addCandidate("Steve1",[10,10,20])
poll.addCandidate("Steve2",[10,10,20])
poll.addCandidate("Steve3",[10,10,20])
poll.addCandidate("Steve4",[10,10,20])

poll.calculateMarginOfError();


