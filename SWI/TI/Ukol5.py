import re



def regex(input_string, pattern):
    """Function that checks whether the input_string matches the pattern"""
    # # any number
    # $ any letter
    # & any character
    for i in pattern:
        if i == '#':
            pattern = pattern.replace(i, r'\d')
        elif i == '$':
            pattern = pattern.replace(i, r'[a-zA-Z]')
        elif i == '&':
            pattern = pattern.replace(i, r'.')

    # Add ^ at the beginning and $ at the end to enforce the pattern to match the entire string
    pattern = '^' + pattern + '$'
    
    fsm = re.compile(pattern)
    if fsm.match(input_string):
        print(f'{input_string} matches the pattern')
    else:
        print(f'{input_string} does not match the pattern')
        

if __name__ == '__main__':
    pattern = "&&*@&&*.$$$*"
    input_strings = ['aaa@aaa.aaa', '131@123.132','ahojako@sa.mas']
    
    for input_string in input_strings:
        regex(input_string, pattern)
        
        
# ZÁVER:
    """
    Verím, že regularne výrazy sú veľmi užitočné a v praxi sa s nimi stretneme často.
    Napríklad pri validácii vstupov od používateľa, alebo pri spracovaní textových súborov.
    """

    
    