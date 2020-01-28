#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. module:: queuereader.py
   :platform: Unix, Windows
   :synopsis: Ulyxes - an open source project to drive total stations and
           publish observation results.
           GPL v2.0 license
           Copyright (C) 2010-2013 Zoltan Siki <siki@agt.bme.hu>

.. moduleauthor:: Bence Turák <turak.bence@epito.bme.hu>
"""
from reader import Reader
from angle import Angle
import queue
import logging
from queuewriter import QueueWriter

class QueueReader(Reader):
    '''Class te read queue
            :param

    '''

    def __init__(self, qu, name=None, filt=None):
        super(QueueReader, self).__init__(name, filt)

        if isinstance(qu, queue.Queue):
            self.q = qu
        elif queue is None:
            self.q = queue.Queue()
        else:
            raise TypeError('qu must be Queue type!')

    def GetQueue(self):
        '''method to get queue
            :returns: queue

        '''
        return self.q
    def GetLine(self):
        '''Get next line from queue
            :returns: next
        '''
        buf = self.q.get()
        res = {}
        for key, val in buf.items():
            if self.filt is None or key in self.filt:
                res[key] = val

        return res


    def GetNext(self):
        '''Get next line from queue
            :returns: next
        '''
        return self.GetLine()

if __name__ == "__main__":
    qu = queue.Queue()

    quWr = QueueWriter(qu = qu)
    data = {'hz': Angle(0.12345), 'v': Angle(100.2365, 'GON'), 'dist': 123.6581}

    quWr.WriteData(data)

    quRe = QueueReader(qu = qu)

    quRe.GetNext()
    quRe.GetQueue()
