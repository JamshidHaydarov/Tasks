def sorting(string : list):
    string2 = string.copy()
    string.sort(key=len)
    string2.sort(key=len, reverse=True)
    return string, string2

sorting(['qw', 'qwey', 'qweryy', 'qwertyyy', 'qwertyyyyy'])