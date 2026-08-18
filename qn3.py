"""2.Given a string s, find the length of the longest substring without
 duplicate characters."""
def length_of_longest_substring(s):
    seen={}
    left=0
    max_length=0
    for right,ch in enumerate(s):
        if ch in seen and seen[ch]>=left:
            left=seen[ch]+1
        seen[ch]=right
        max_length=max(max_length,right-left+1)
    return max_length

str="abcdeabcdefbb"
print(length_of_longest_substring(str))