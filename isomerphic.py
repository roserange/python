def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        if s_char in s_map:
            if s_map[s_char] != t_char:
                return False
        else:
            s_map[s_char] = t_char

        if t_char in t_map:
            if t_map[t_char] != s_char:
                return False
        else:
            t_map[t_char] = s_char

    return True
