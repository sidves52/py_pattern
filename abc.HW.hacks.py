def abc_order():
    print('Enter the words that must be put in sequence with a space between them.')
    print('\n'.join(sorted([x.lower() for x in input().split()])))

abc_order()