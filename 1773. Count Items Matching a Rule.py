def countMatches(items, ruleKey: str, ruleValue: str) -> int:
    matched = 0
    for item in items:
        if ruleKey == 'type':
            if item[0] == ruleValue:
                matched += 1
        if ruleKey == 'color':
            if item[1] == ruleValue:
                matched += 1
        if ruleKey == 'name':
            if item[2] == ruleValue:
                matched += 1
    return matched