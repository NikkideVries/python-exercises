# is_two function:
def is_two(n):
    if n in (2, '2', 2.0):
        return True
    else:
        return False
    

# is_vowel function:
def is_vowel(string):
    if type(string) == str:
        if len(string) == 1 and string.isalpha():
            return string.lower() in list('aeiou')
        else: 
            return False
    else:
        return False
    
# is_consonat function:
def is_consonant(somestring):
    """
    This function will:
    - intially check the input is a string
        - and 1 char long
        - and a letter
            -if true, returns the opposite return of is_vowel, using the NOT operator
            - False otherwise
    -returns False if not a string
    """
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha():
            return (not is_vowel(somestring))
        else:
            return False
    else: 
        return False

# capitalize_starting_consonant: 
def capitalize_starting_consonant(word):
    """
    This function will initially check if:
    - input is a str
        - checks if 1st char of the input is a consonant
            - if True, returns the inputted string w/1st char Capitalized
            - False otherwise
        - returns False if not a string
    """
    if type(word) == str:
        if is_consonant(word[0]):
            return word.capitalize()
        else:
            return f"{word} doesn't start with a consonant."
    else:
        return f"{word} isn't a string."
    
# calculate_tip
def calculate_tip(bill, tip_percent=.2):
    """
    tip_percent is a float number between 0-1
    """
    return f"{tip_percent*100}% tip is: $ {round(bill * tip_percent,2)}"

# apply_discount
def apply_discount(orig_price, discount_pct):
    return (1 - discount_pct)* orig_price

# handle_commas
def handle_commas(fakenum):
    """
    This function will:
    - check if input is a string
        -removes any commas
        -check if the stripped input is a digit
            - if True, returns input as an integer
            -False otherwise
    - if not a string, returns false stmt
    """
    if type(fakenum) == str:
        stripfakenum = fakenum.replace(",", "")
        if stripfakenum.isdigit():
            return int(stripfakenum)
        else:
            return False
    else:
        False
        
# get_letter_grade 
def get_letter_grade(somegrade):
    if type(somegrade) == int:
        if somegrade >= 90:
            return 'A'
        elif somegrade >= 80:
            return 'B'
        elif somegrade >= 70:
            return 'C'
        elif somegrade >= 60:
            return 'D'
        else: return 'F'
    else:
        return f"{somegrade} is not a digit."


#remove_vowels
def remove_vowels(word):
    new_word = ""
    for letter in word:
        if not is_vowel(letter):
            new_word += letter
    return new_word

# normalize_name
def normalize_name(somestring):
    
    newstring = ""
    
    for letter in somestring.strip():

        if letter.isalnum() or letter == " ":
            
            newstring += letter
    
    for letter in newstring:
      
        if letter.isalpha():
            
            break
        else:
       
            newstring = newstring[1:]
            
    return newstring.lower().replace(" ", "_")

#