def plusOne(digits):
    intList_to_stringList = list(map(str, digits))
    string = ''.join(intList_to_stringList)
    int_number = int(string)
    plus_one = int_number + 1

    returned_list = list(map(int, str(plus_one)))
    return returned_list

print(plusOne([4,9,9,9]))