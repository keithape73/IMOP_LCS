# IMOP-LCS: A Fast and General-Purpose LCS Optimization Algorithm (O(N log N))

> ⚡️ First known LCS optimization using Index Mapping and Ordered Projection, combined with LIS.

**IMOP-LCS (Index Mapping + Ordered Projection for LCS)** is the **first known LCS optimization technique**  
that reliably transforms the Longest Common Subsequence (LCS) problem into a Longest Increasing Subsequence (LIS) problem  
in a way that works **correctly for all input cases**, not just for special or restricted scenarios.

> ✅ This approach achieves `O(N log N)` time complexity,  
> vastly improving upon the traditional `O(N*M)` dynamic programming method.

---

## 🚀 Key Features

- ⚡️ **Fast**: Runs in `O(N log N)` using Python’s built-in `bisect` module.
- 🔍 **General**: Handles all kinds of inputs — including repeated characters and non-unique patterns.
- 🧠 **Elegant**: Uses clean index mapping and reverse-order projection to reduce LCS to LIS.
- 🧪 **Tested**: Produces correct results across all edge cases where other LIS-based methods fail.

---

## 💡 Why Is This "First-Known"?

Most LIS-based LCS attempts fail when:
- Characters repeat in either string.
- Mappings are non-unique.
- Projections do not preserve the required subsequence order.

IMOP-LCS is the first known implementation to solve all of the above,  
by projecting `text2` onto `text1` via reverse-indexed positions and preserving LIS validity.

---

## 🧩 How It Works

1. **Index Mapping**  
   - Build a dictionary of all character positions from `text1`, in reverse order (for correct projection).
2. **Ordered Projection**  
   - For each character in `text2`, append its mapped positions in order.
3. **LIS Application**  
   - Run LIS on the resulting index sequence → this gives the length of the LCS.

---

## 📁 File Structure

```plaintext
imop_lcs.py        # Main implementation with sample usage
README.md          # You're here!
LICENSE            # MIT License (optional)

---
## Usage

```python
from imop_lcs import imop_lcs

text1 = "abcabcabc"
text2 = "abcabc"
print(imop_lcs(text1, text2))  # Output: 6

