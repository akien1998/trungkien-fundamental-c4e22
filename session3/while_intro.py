while True:
    pass_word=(input("enter pass : ? "))
    l = len(pass_word)
    if not pass_word.isdigit() and l>8 :
        print('True')
        break
    elif pass_word.isupper():
        print("Flase")
        print('False input again')
    elif pass_word.lower():
        print("false")
        print('False input again')

    

        
        