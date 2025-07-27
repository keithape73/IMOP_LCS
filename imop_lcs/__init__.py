"""
IMOP-LCS (Index Mapping + Ordered Projection for LCS)

Author: Dongjun Kim (keithape73)
Description:
    First known O(N log N) algorithm to solve Longest Common Subsequence (LCS)
    using index mapping and LIS (Longest Increasing Subsequence).
"""

from .imop_lcs import imop_lcs

__all__ = ['imop_lcs']
