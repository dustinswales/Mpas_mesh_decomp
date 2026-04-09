#!/usr/bin/env python
import os
import sys
import argparse

#
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--decomps', help='MPI decompositions, separated by a space', nargs='*', type=int, required=False)
#
def parse_args():
    args    = parser.parse_args()
    decomps = args.decomps
    return decomps
#
def main():
#
    (decomps) = parse_args()
    print("SWALES",decomps)
    for decomp in decomps:
        print("gpmetis -minconn -contig -niter=200 x1.${{matrix.mesh}}.graph.info ",decomp)
    # end for
#
if __name__ == '__main__':
    main()
