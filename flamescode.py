def flames(name1, name2):
    """
    Calculate the FLAMES result for two names.

    Args:
        name1 (str): The first name.
        name2 (str): The second name.

    Returns:
        str: The FLAMES result.
    """
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # Calculate the length of the names
    len1 = len(name1)
    len2 = len(name2)

    # Create a list to store the common letters
    common = []

    # Iterate through the letters of the first name
    for letter in name1:
        # Check if the letter is in the second name and not already in common
        if letter in name2 and letter not in common:
            common.append(letter)

    # Calculate the FLAMES result
    flames_result = len1 + len2 - 2 * len(common)

    # Define the FLAMES meanings
    flames_meanings = {
        1: "F - Friends",
        2: "L - Lovers",
        3: "A - Affection",
        4: "M - Marriage",
        5: "E - Enemies",
        6: "S - Siblings"
    }

    # Return the FLAMES result
    return flames_meanings.get(flames_result % 6, "Unknown")

# Example usage
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

result = flames(name1, name2)
print("FLAMES Result:", result)