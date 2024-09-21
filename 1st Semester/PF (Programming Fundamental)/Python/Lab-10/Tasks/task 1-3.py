def noTabs(string):
    strLength = len(string)
    i = 0
    removedTabs = ''
    while(i < strLength):
        if(string[i] == '\t'):
            removedTabs += '   '
        else:
            removedTabs += string[i]
        i += 1
    return removedTabs

string = 'Programming\tis not\thard, but\tits\tnot easy'
print("String with Tabs:", string)
print("String without Tabs:", noTabs(string))
        