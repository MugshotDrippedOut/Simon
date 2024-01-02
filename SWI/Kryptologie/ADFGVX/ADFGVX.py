import string
import unidecode
import random

def create_alphabet(numbers = False):
    alphabet = []
    for i in string.ascii_uppercase:
        alphabet.append(i)
    if numbers == False:
        alphabet.remove("Q")
    if numbers == True:
        for i in range(0,10):
            alphabet.append(str(i))
    return alphabet

def alphabet_shuffle(alphabet, seed):
    random.seed(seed)
    random.shuffle(alphabet)
    return alphabet


def create_table(alphabet, numbers = False):
    table = []
    rowsCols = 5
    if numbers == True:
        rowsCols = 6
    for i in range(0,rowsCols):
        table.append(alphabet[i*rowsCols:i*rowsCols+rowsCols])
    return table


def sanitize_text(text, alphabet, numbers = False):
    text = text.upper()
    text = unidecode.unidecode(text)
    text = text.replace(" ","XZYSPACE")
    if numbers == False:
        text = text.replace("Q","O")
        for i in text:
            if i not in alphabet:
                text = text.replace(i,"")
    for i in text:
        if i not in alphabet:
            text = text.replace(i,"")
        
    return text


def str_to_pairs(text):
    pairs = []
    if len(text)%2 != 0:
        text += " "
    for i in range(0,len(text)):
        if i%2 == 0:
            pairs.append([text[i],text[i+1]])
    return pairs


def get_index(table, letter):
    for i in range(0,len(table)):
        for j in range(0,len(table[i])):
            if table[i][j] == letter:
                return i,j
    return -1,-1


def substitute(pairs, table):
    ADFGVX = []
    for i in range(0,len(pairs)):
        ADFGVX.append(get_index(table, pairs[i][0])[0])
        ADFGVX.append(get_index(table, pairs[i][0])[1])
        ADFGVX.append(get_index(table, pairs[i][1])[0])
        ADFGVX.append(get_index(table, pairs[i][1])[1])
    return ADFGVX


def all_indexes_to_ADFGVX(pairs, table, numbers=False):
    adfgvx = "ADFGX"
    if numbers == True:
        adfgvx = "ADFGVX"
    indexes = []
    encrypted = []
    for i in range(0,len(pairs)):
        indexes.append(get_index(table, pairs[i]))
        encrypted.append(adfgvx[indexes[i][0]])
        encrypted.append(adfgvx[indexes[i][1]])            
    return encrypted


def sanitize_key(key):
    key = key.upper()
    key = key.replace(" ","")
    key = unidecode.unidecode(key)
    klist = []
    for i in key:
        klist.append(i)
    aaa = {}
    for i in range(0,len(klist)):
        if klist[i] not in aaa:
            aaa[klist[i]] = 1
        else:
            count = aaa[klist[i]]
            aaa[klist[i]] += 1
            klist[i] += str(count)
    return klist


def transposition_table(ADFGVX, key):
    table = []
    for i in range(0,len(key)):
        table.append([])
    for i in range(0,len(ADFGVX)):
        table[i%len(key)].append(ADFGVX[i])
    return table

 
def sort_array(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


def transposition_table_alphabeticly_with_key(ADFGVX, key):
    table = []
    for i in key:
        table.append([])
        table[key.index(i)].append(i)
    for i in range(0,len(ADFGVX)):
        table[i%len(key)].append(ADFGVX[i])
    table = sort_array(table)
    table = [i[1:] for i in table]
    return table


def encrypt(plainText, key, tableSeed, numbers = False):
    alphabet = create_alphabet(numbers)
    s_a = alphabet_shuffle(alphabet, tableSeed)
    s_key = sanitize_key(key)
    tablea = create_table(s_a, numbers)
    return transposition_table_alphabeticly_with_key(all_indexes_to_ADFGVX(sanitize_text(plainText, alphabet, numbers),tablea, numbers),s_key)


def list_to_str(given_list):
    str_list = ""
    for i in given_list:
        for j in i:
            str_list += j
    return str_list
    #return str(encrypt).replace("[","").replace("]","").replace(",","").replace("'","").replace(" ","")


def appent_to_item_every_character(item, string):
    for i in string:
        item.append(i)
    return item


## @brief This function creates a reverse transposition table with a password.
#  
#  @param ADFGVX A list of characters to be transposed.
#  @param key A string that serves as the key for the transposition.
#  
#  @return A list of lists, where each inner list represents a row in the transposition table.
#  
#  The function first calculates the number of longer arrays and the number of characters in shorter arrays.
#  It then creates an empty table and fills it with empty lists.
#  The function then sorts the key and creates an array of unsorted keys.
#  It then iterates over the key, and for each character in the key, it appends the corresponding characters from ADFGVX to the table.
#  Finally, it separates the table into individual characters and returns the separated table.
def transpose_with_key(ADFGVX, key):
    # Initialize the table
    table = []
    # Calculate the number of longer arrays and the number of characters in shorter arrays
    number_of_longer_arrays = len(ADFGVX)%len(key)
    number_of_characters_in_shorter_arrays = int(len(ADFGVX)/len(key))
    # Fill the table with empty lists
    for i in key:
        table.append([])
        table[key.index(i)].append(i)
    # Create an array of unsorted keys
    unsorted_key = [i[0] for i in table]
    unsorted_key_arr = []
    # Sort the key
    sort_key = sort_array(key)
    # Fill the unsorted_key_arr with the indices of the sorted keys in the unsorted keys
    for i in range(0,len(sort_key)):
        unsorted_key_arr.append(unsorted_key.index(sort_key[i]))
    counter = 0
    # Iterate over the key
    for i in key:
        # For each character in the key, append the corresponding characters from ADFGVX to the table
        for j in unsorted_key_arr:
            if i == unsorted_key[j]:
                if j < number_of_longer_arrays:
                    table[counter].append(ADFGVX[0:number_of_characters_in_shorter_arrays+1])
                    ADFGVX = ADFGVX[number_of_characters_in_shorter_arrays+1:]
                else:
                    table[counter].append(ADFGVX[0:number_of_characters_in_shorter_arrays])
                    ADFGVX = ADFGVX[number_of_characters_in_shorter_arrays:]
        counter += 1
    # Separate the table into individual characters
    table = [i[1:] for i in table]
    separated = []
    for i in table:
        separated.append([j for j in i[0]])
    # Return the separated table
    return separated


def resort_table(table, key):
    unsorted_key = [i for i in key]
    sorted_key = sort_array(key)
    for i in range(0,len(key)):
        table[i].insert(0,sorted_key[i])
    new_table = []
    for i in range(0,len(key)):
        for j in range(0,len(key)):
            if table[j][0] == unsorted_key[i]:
                new_table.append(table[j])
    new_table = [i[1:] for i in new_table]
    return new_table
        


def twoD_to_str(table):
    out = ""
    biggest = max([len(i) for i in table])
    for i in range(0,biggest):
        for j in table:
            if len(j)>i:
                out += j[i]   
    return out

def ADFGVXtext_to_indexes(ADFGVX_text, numbers = False):
    adfgvx = "ADFGX"
    if numbers == True:
        adfgvx = "ADFGVX"
    indexes = []
    for i in range(0,len(ADFGVX_text)):
        indexes.append(adfgvx.index(ADFGVX_text[i]))
    return indexes
    
    

def cipher_text_to_text(cipher_text, seed, numbers = False):
    shuffuled_alphabet = alphabet_shuffle(create_alphabet(numbers), seed)
    table = create_table(shuffuled_alphabet, numbers) 
    indexes = str_to_pairs(ADFGVXtext_to_indexes((cipher_text), numbers))
    final = []
    for i in indexes:
        final.append(table[i[0]][i[1]])
    return final

def decrypt(cipher_text, key, tableSeed, numbers = False):
    decrypted = (cipher_text_to_text(twoD_to_str(resort_table(transpose_with_key(cipher_text, sanitize_key(key)), sanitize_key(key))), tableSeed, numbers))
    return list_to_str(decrypted)

def unfilter_spaces(string):
    return string.replace("XZYSPACE"," ")

def space_every_n_characters(string, n):
    out = ""
    for i in range(0,len(string)):
        out += string[i]
        if i%n == n-1:
            out += " "
    return out


def space_based_on_ttawk(ttawk):
    out = ""
    for i in ttawk:
        out += space_every_n_characters(list_to_str(i),len(i)) + " "
    return out

def remove_spaces(string):
    return string.replace(" ","")


def check_for_not_ADFGX(string):
    for i in string:
        if i not in "ADFGX":
            return True
    return False

def check_for_not_ADFGVX(string):
    for i in string:
        if i not in "ADFGVX":
            return True
    return False


def print_encrypted(plainText, key, tableSeed, numbers = False, everything = True):
    alphabet = create_alphabet(numbers)
    if everything == True:
        print("Alphabet:          " + str(alphabet))
    s_a = alphabet_shuffle(alphabet, tableSeed)
    if everything == True:
        print("Shuffled alphabet: " + str(s_a))
    tablea = create_table(s_a, numbers)
    if everything == True:
        print("Plain text: " + plainText)
        print("Key: " + key)
        print("Table seed: " + tableSeed)
        print("Table: ")
        for i in tablea:
            print(i)
    print("Sanitized text: " + sanitize_text(plainText, alphabet, numbers))
    print("Pairs: " + str(str_to_pairs(sanitize_text(plainText, alphabet, numbers))))
    print("Substituted pairs: " + str(substitute(str_to_pairs(sanitize_text(plainText, alphabet, numbers)), tablea)))
    print("ADFGVX: " + str(all_indexes_to_ADFGVX(sanitize_text(plainText, alphabet, numbers),tablea, numbers)))
    print("Sanitized password: " + str(sanitize_key(key)))
    print("Transposition table: ")
    for i in transposition_table(all_indexes_to_ADFGVX(sanitize_text(plainText, alphabet, numbers),tablea),sanitize_key(key)):
        print(i)
    print("Sorted password: " + str(sort_array(sanitize_key(key))))
    for i in transposition_table_alphabeticly_with_key(all_indexes_to_ADFGVX(sanitize_text(plainText, alphabet, numbers),tablea, numbers),(sanitize_key(key))):
        print(i)

    print("Encrypted: " + str(encrypt(plainText, key, tableSeed, numbers)))
    print("Encrypted to text: " + list_to_str(encrypt(plainText, key, tableSeed, numbers)))
    print("\n")


def print_decrypted(crypted_text, key, seed, numbers):
    print("Encrypted: " + str(crypted_text))
    print("Shuffled alphabet table: " + str(create_table(alphabet_shuffle(create_alphabet(numbers), seed), numbers)))
    print("Decrypted to ADFGVX: " + str(transpose_with_key(crypted_text, sanitize_key(key))))
    print("Resorted table: " + str(resort_table(transpose_with_key(crypted_text, sanitize_key(key)), sanitize_key(key))))
    print("Indexes: " + str(ADFGVXtext_to_indexes(twoD_to_str(resort_table(transpose_with_key(crypted_text, sanitize_key(key)), sanitize_key(key))), numbers)))
    print("Cipher text: " + str(cipher_text_to_text(twoD_to_str(resort_table(transpose_with_key(crypted_text, sanitize_key(key)), sanitize_key(key))), seed, numbers)))
    print("Decrypted: " + str(decrypt(crypted_text, key, seed, numbers)))
    print("\n")


if __name__ == '__main__':
    plainText = "Aho j"
    key = "Kolotoc"
    tableSeed = "Seed"
    print_encrypted(plainText, key, tableSeed, False, True)
    #print_encrypted("12034", key, tableSeed, True, False)
    a = list_to_str(encrypt(plainText, key, tableSeed, False))
    print(a)

    print_decrypted(a, key, tableSeed, False)
    pass