#!/usr/bin/env python
import os
import sys
import argparse

#
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--decomps', help='MPI decompositions, separated by a space', nargs='*', type=int, required=True)
parser.add_argument('-m', '--mesh',    help='mesh',type=int,required=True)
#
def parse_args():
    args    = parser.parse_args()
    decomps = args.decomps
    mesh    = args.mesh
    return (mesh, decomps)
#
def main():
#
    (mesh, decomps) = parse_args()
    for decomp in decomps:
        com = "gpmetis -minconn -contig -niter=200 x1."+str(mesh)+".graph.info "+str(decomp)
        result = os.system(com)
    # end for

    # Create tarball with graph files
    com = "tar -cvf x1."+str(mesh)+".graph.info.tar x1."+str(mesh)+".graph.info.*"
    result = os.system(com)
#
if __name__ == '__main__':
    main()
