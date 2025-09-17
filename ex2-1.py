list_of_strings = "abc", "def", "ghi", "jkl", "mno", "def", "pqr", "stu", "vwx", "yz"

def recursive_duplicates_check(s):
    if len(s) <= 1:
        return False
    if s[0] in s[1:]:
        return True
    
    return recursive_duplicates_check(s[1:])


def good_duplicates_check(string_list):
    if len(string_list) > len(set(string_list)):
        return True
    return False

def main():
    if good_duplicates_check(list_of_strings):
        print("Duplicates found (good)")
    else:
        print("No duplicates (good)")
    if recursive_duplicates_check(list_of_strings):
        print("Duplicates found (recursive)")
    else:
        print("No duplicates (recursive)")

if __name__ == "__main__":
    main()
