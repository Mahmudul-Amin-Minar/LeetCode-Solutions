def mostWordsFound(sentences) -> int:
    len_sen = []
    for i in sentences:
        len_sen.append(len(i.split()))
    return max(len_sen)