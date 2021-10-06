def addToArrayForm(A, K):
    intList_to_stringList = list(map(str, A))
    string = ''.join(intList_to_stringList)
    int_number = int(string)
    plus_K = int_number + K

    returned_list = list(map(int, str(plus_K)))
    return returned_list

print(addToArrayForm([1,2,0,0], 34))