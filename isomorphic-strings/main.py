

def isIsomorphic(s, t):
    map_s_to_t = {}

    for char_s, char_t in zip(s, t):
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t

        
    return len(set(t)) == len(map_s_to_t)

print(isIsomorphic("bbbaaaba", "aaabbbba"))
