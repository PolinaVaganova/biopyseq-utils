from typing import Union, Sequence, List

DNA_DNA_PAIRS = {'A': 'T',
                 'T': 'A',
                 'C': 'G',
                 'G': 'C'}

RNA_DNA_PAIRS = {'A': 'T',
                 'U': 'A',
                 'C': 'G',
                 'G': 'C'}

RNA_RNA_PAIRS = {'A': 'U',
                 'U': 'A',
                 'C': 'G',
                 'G': 'C'}

NUCLEOTIDE_NAMES = ['A', 'T', 'C', 'G', 'U']


# function for getting a rna transcript, based on dna sequence
def transcribe(seq: str) -> str:
    """
    Calculate rna transcript seq from dna seq

    :param seq:
    - seq (str): dna seq

    :return:
    - str: rna transcript seq
    """
    pass


# function for getting a dna, based on rna transcript
def reverse_transcribe(seq: str) -> str:
    """
    Calculate dna complementary seq from rna seq

    :param seq:
    - seq (str): rna seq

    :return:
    - str: complementary dna seq
    """
    pass


def reverse(seq: str) -> str:
    """
    Get reverse seq for dna or rna

    :param seq:
    - seq (str): dna or rna seq

    :return:
    - str: reverse seq
    """
    pass


# function for getting a complementary sequence for dna or rna
def complement(seq: str) -> str:
    """
    Create complementary seq for dna or rna (if unclear will be treated as dna)

    :param seq:
    - seq (str): dna or rna seq

    :return:
    - str: complementary seq
    """
    pass


# function for getting a complementary sequence for dna or rna in reverse format
def reverse_complement(seq: str) -> str:
    """
    Create complementary seq for dna or rna in reverse format (if unclear will be treated as dna)

    :param seq:
    - seq (str): dna or rna seq

    :return:
    - str: complementary seq in reverse format
    """
    pass


# function for count nucleotides in seq
def count_nucleotides(seq: str) -> str:
    """
    Characterize percentages of each type of nucleotide

    :param seq:
    - seq (str): dna or rna seq

    :return:
    - str: each nucleotide with it percentage weight
    """
    pass


def make_triplets(seq: str) -> list:
    """
    Split your seq into triplets

    :param:
    - seq (str): dna or rna seq

    :return:
    - List[str]: created triplets
    """
    pass


# function for check a sequence correctness
def is_dna_or_rna(seq: str) -> bool:
    """
    Check if seq dna/rna or not

    :param:
    - seq (str): dna or rna seq

    :return:
    - bool: the result of the check
    """
    pass
