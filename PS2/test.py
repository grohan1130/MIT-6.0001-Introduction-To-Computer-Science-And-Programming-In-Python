import string

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    all_letters_string = string.ascii_lowercase
    all_letters_list = [*all_letters_string]
    # for i in range(len(all_letters_list)):
    #    if all_letters_list[i] not in letters_guessed:
    for element in letters_guessed:
        all_letters_list.remove(element)
    return ''.join(all_letters_list)

print(get_available_letters(['a','z','c']))
    
