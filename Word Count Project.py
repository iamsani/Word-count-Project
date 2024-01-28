def count(input):
    """
    Count the number of words in the input.


    Returns:
    - int: The word count.
    """
    # Split the input text
    words = input.split()

    # Return the count of words
    return len(words)


def main():
    print("Welcome to the Word Counting Project")

    # Prompt the user to enter a sentence or paragraph
    user = input("Enter a sentence or paragraph: ")


    try:
        # Check if the input is empty
        if not user.strip():
            raise ValueError("Input is empty.")

        # Call the count function
        word = count(user)

        # Display the word count
        print(f"Word Count: {word}")

    except ValueError as hehe:
        # Handle empty input or other potential errors
        print(f"Error: {hehe}")


if __name__ == "__main__":
    main()

