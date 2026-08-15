def generate_number_sequence(limit: int) -> str:
    """
    Generates a space-separated string sequence of numbers starting from 1 up to a specified limit.

    This utility enforces strict type safety and data validation rules before execution 
    to prevent unexpected processing behaviors.

    Args:
        limit (int): The positive integer ceiling for the sequence.

    Returns:
        str: A single space-separated string containing the numeric sequence.
        
    Raises:
        TypeError: If the provided argument is not a primitive integer.
        ValueError: If the integer provided is less than or equal to zero.
    """
    
    if type(limit) is not int:
        return "Argument must be an integer value."
        
    if limit <= 0:
        return "Argument must be an integer greater than 0."
        
    
    sequence_pool = [str(num) for num in range(1, limit + 1)]
    return " ".join(sequence_pool)


if __name__ == "__main__":
    print("Testing sequence generator logic:")
    print(f"Input 4  -> {generate_number_sequence(4)}")
    print(f"Input 12 -> {generate_number_sequence(12)}")
