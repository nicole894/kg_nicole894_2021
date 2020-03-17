import sys
from collections import defaultdict

def main(str1, str2):
    
    if len(str1) != len(str2):
        return False
    else:
        str_list1 = list(str1)
        str_list2 = list(str2)
        mapping_dict = defaultdict()
        for i in range(len(str_list1)):
            if str_list1[i] in mapping_dict.keys():
                mapped_key = mapping_dict[str_list1[i]]
                if mapped_key != str_list2[i]:
                    return False
            else:
                mapping_dict.update({str_list1[i]:str_list2[i]})

        return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong number of arguments passed.")
    else:
        string_1 = sys.argv[1]
        string_2 = sys.argv[2]
        hasOneMapping = main(string_1, string_2)
        if hasOneMapping:
            print("true")
        else:
            print("false")
