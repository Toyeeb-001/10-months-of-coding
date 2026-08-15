def caesar_cipher_engine(text, shift, encrypt=True):

    
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    
    if not encrypt:
        shift = - shift
    
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt_message(text, shift):
    return caesar_cipher_engine(text, shift)
    
def decrypt_message(text, shift):
    return caesar_cipher_engine(text, shift, encrypt=False)


secret_output = encrypt_message('SecureData2026', 3)
print(secret_output)
