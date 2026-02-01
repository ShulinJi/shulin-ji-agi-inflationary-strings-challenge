# Shulin-Ji-agi-inflationaryStrings--challenge

## How to Run
Make sure you have Python 3 installed.

```bash
python theAdvantageGroup.py

## Design
The program scans the string from left to right.

At each position, it tries to match a number word starting at that index.
Different number words have different lengths, so longer words are checked first to avoid partial matches (for example, matching seven before seventeen).

If a match is found, it replaces the word with the next number word and moves the pointer forward by the length of the match.
If no match is found, it simply copies the current character and moves forward by one.

Time complexity: O(n * k), k is the lenghth of possible word match, n is the length of given string
Space complexity: O(n), n is the length of given string
## Tradeoffs
To keep the solution simple and reasonable for a 45-minute exercise, the program only supports number words from zero to twenty.
Handling patterns beyond this range (like twenty one or one hundred) would require more complex parsing logic, which was intentionally left out.
However, the current program has very limited ways to scale for large number ranges!
