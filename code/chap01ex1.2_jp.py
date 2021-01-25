from __future__ import print_function

"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

""" base file: chap01ex.py. for solution, compare with chap01soln.py """

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df


def ValidatePregNum(resp):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)


    # iterate over pregnum Series, which provides indices for each respondent
    # and number of pregnancies recorded for that respondent
    for index, pregnum in resp.pregnum.items():
        # fetch caseid associated with current index/respondent
        caseid = resp.caseid[index]
        # fetch records associated with caseid
        indices = preg_map[caseid]

        if len(indices) != pregnum:
            # number of records in pregnancy data doesn't match number of
            # pregnancies in respondent data; something went wrong
            print(caseid, len(indices), pregnum)
            return False

    return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    resp = ReadFemResp()
    print(resp.pregnum.value_counts())

    ValidatePregNum(resp)
    
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
