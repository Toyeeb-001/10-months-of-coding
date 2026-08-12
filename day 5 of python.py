def caesar():

    text = 'hello world'
    shift = 5
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    encrypted_text = text.translate
    print(encrypted_text) 
