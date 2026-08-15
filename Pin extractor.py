def extract_pin_from_poem(poem: str) -> str:
    """
    Extracts a secure PIN code from a structured poem sequence.
    
    The algorithm processes each line sequentially. It evaluates the word 
    at the index matching the current line number, and appends its character length 
    to the generated key. If the line does not contain enough words, it defaults to '0'.
    
    Args:
        poem (str): A newline-separated multi-line string containing the text.
        
    Returns:
        str: The extracted numeric string PIN code.
    """
    # Guard clause: Handle empty or invalid inputs gracefully
    if not poem or not isinstance(poem, str):
        return "0"

    secret_code = []
    lines = poem.strip().split('\n')
    
    for line_index, line in enumerate(lines):
        words = line.split()
        
        try:
            # Check if the line has enough words to match the current index line position
            if len(words) > line_index:
                word_target = words[line_index]
                # Strip out punctuation markers so they don't corrupt the digit extraction length
                clean_word = "".join(char for char in word_target if char.isalnum())
                secret_code.append(str(len(clean_word)))
            else:
                secret_code.append('0')
        except (IndexError, TypeError):
            # Defensive programming fallback to ensure the algorithm never crashes in production
            secret_code.append('0')
            
    return "".join(secret_code)


def batch_process_poems(poems_list: list) -> list:
    """
    Processes a collection of poems to extract a batch list of hidden security keys.
    
    Args:
        poems_list (list): A collection of multi-line strings.
        
    Returns:
        list: A collection of extracted string PIN codes.
    """
    if not isinstance(poems_list, list):
        raise TypeError("Input must be a valid list of strings.")
        
    return [extract_pin_from_poem(poem) for poem in poems_list]
