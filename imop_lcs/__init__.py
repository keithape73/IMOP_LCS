"""
IMOP-LCS (Index Mapping + Ordered Projection for LCS)

Author: Dongjun Kim (keithape73)
Description:
    First known O(N log N) algorithm to solve Longest Common Subsequence (LCS)
    using index mapping and LIS (Longest Increasing Subsequence).
"""
__version__ = "1.0.0"
__author__ = "Dongjoon Kim (keithape73)"

from .imop_lcs import imop_lcs

__all__ = ['imop_lcs']
