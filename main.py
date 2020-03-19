import sys

def main(s1, s2):
    return does_it_map(s1, s2)
    
def does_it_map(s1, s2):
    if num_unique_char(s1) >= num_unique_char(s2):
        return True
    return False

def num_unique_char(s):
    count = 0
    used_chars = []
    for i in s:
        if i not in used_chars:
            count+=1
            used_chars.append(i)
    return(count)

print(main(sys.argv[1], sys.argv[2]))

