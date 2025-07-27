import bisect

def imop_lcs(text1: str, text2: str) -> int:
    """
    Fast LCS algorithm using Index Mapping + Ordered Projection + LIS.
    Time Complexity: O(N log N)
    Works for all input cases (including repeated characters).
    """ 
    # 1. Index Mapping (reverse order)
    pos_map = {}
    for i, char in enumerate(text1):
        if char not in pos_map:
            pos_map[char] = []
        pos_map[char].append(i)

    for char in pos_map:
        pos_map[char].reverse()
      
    # 2. Ordered Projection: text2 → text1's index sequence
    sequence = []
    for char in text2:
        if char in pos_map:
            sequence.extend(pos_map[char])
        
    return lis(sequence)  
    
    # 3. LIS on the projected indices
def lis(arr: list) -> int:
    if not arr:
        return 0

    tails = [] 

    for num in arr:
        idx = bisect.bisect_left(tails, num)
        
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
           
    return len(tails)
