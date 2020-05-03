"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp():
    return nsfg.ReadFemResp()

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('Running')
    resp = ReadFemResp()
    print(resp.pregnum.value_counts().sort_index())

    preg = nsfg.ReadFemPreg()
    pm = nsfg.MakePregMap(preg)

    print('checking counts')
    for i, r in resp.caseid.head().iteritems():
        if resp.pregnum[i] != len(pm[r]):
            print([r, resp[resp.caseid == r].pregnum.iloc[0], len(pm[r])])



    #print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
