#!/usr/bin/env python

from Bio import AlignIO
from Bio.Alphabet import IUPAC,Gapped
import sys

# This script takes an alignment of de novo assemblies to a reference and merges
# it with reference guided assemblies to the same reference sequence

# check for correct arguments
if len(sys.argv) != 5:
    print("Usage: FastaToNexus.py <denovo file> <refguided file> <reference \
    name> <outputfile>")
    sys.exit(0)

deNovoName = sys.argv[1]
refFileName = sys.argv[2]
reference = sys.argv[3]
outFileName = sys.argv[4]

deNovoFile = open(deNovoName, 'r')
refFile = open(refFileName, 'r')
outFile = open(outFileName. 'w')

deNovoAlign = AlignIO.read(deNovoFile, 'fasta', 
    alphabet=Gapped(IUPAC.ambiguous_dna, '-'))
refAlign = AlignIO.read(refFile, 'nexus')


AlignIO.write(alignment, outFile, 'nexus')

deNovoFile.close()
refFile.close()
outFile.close()