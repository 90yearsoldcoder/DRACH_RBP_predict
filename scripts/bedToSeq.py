from pybedtools import BedTool

import pybedtools

def get_sequence(chromosome, start, end, strand, reference):
    """
    Retrieve a DNA sequence from a specified region of a reference genome using pybedtools.
    
    Args:
    chromosome (str): The chromosome identifier (e.g., 'chr1', 'chr2', etc.).
    start (int): The start position in the chromosome (0-based index).
    end (int): The end position in the chromosome (exclusive).
    strand (str): Strand information ('+' for forward, '-' for reverse).
    reference (str): Path to the reference genome in FASTA format.
    
    Returns:
    str: The DNA sequence from the specified region, adjusted for strand.
    """
    # Create a BedTool object from a string defining the region
    region = f"{chromosome}\t{start}\t{end}\t.\t0\t{strand}"
    bedtool = pybedtools.BedTool(region, from_string=True)
    
    # Get the sequence associated with the region
    sequence = bedtool.sequence(fi=reference, s=True)
    
    # Read the sequence from the output file
    with open(sequence.seqfn) as f:
        next(f)  # skip header
        sequence = f.read().strip()
    
    return sequence

if __name__=='__main__':
    ref = '/restricted/projectnb/benwol/jmh/script/ref/human/hg38_111/Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa'
    seq = get_sequence('5', 10000, 10005, '+', ref)
    print(seq)