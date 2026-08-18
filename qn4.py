"""
TO retrieve the longest substring without duplicate characters
"""
def longest_substring(s):
    seen=set()
    current=""
    longest=""
    for ch in s:
        if ch in seen:
            seen=set([ch])
            current = ch
        else:
            seen.add(ch)
            current += ch
        if len(current) > len(longest):
            longest = current
    return longest  
string="abcdeabcdefbb"
print(longest_substring(string))