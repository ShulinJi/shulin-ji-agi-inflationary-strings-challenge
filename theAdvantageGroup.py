ONES = [
    "zero","one","two","three","four","five","six","seven","eight","nine",
    "ten","eleven","twelve","thirteen","fourteen","fifteen",
    "sixteen","seventeen","eighteen","nineteen", "twenty"
]

# we should sort based on the length to avoid cases like seven gets matched before seventeen
WORDS_BY_LENGTH = sorted(ONES, key=len, reverse=True)
NEXT = {}

# pre-compute the word to next word mapping
def compute_next_words() -> None:
    for i in range(len(ONES) - 1):
        NEXT[ONES[i]] = ONES[i + 1]
    return 

def inflate(text: str) -> str:
    result_chars = []
    curr_pos = 0

    while curr_pos < len(text):
        matched_word = None
        # we try to match a number word starting at current position with different possible lengths, from biggest to smallest
        for word in WORDS_BY_LENGTH:
            end = curr_pos + len(word)
            if end <= len(text) and text[curr_pos:end].lower() == word:
                matched_word = word
                break
        
        # if we found a mtch for the current number, we replace it with the next number word
        if matched_word is not None:
            replacement = NEXT.get(matched_word, matched_word)
            result_chars.append(replacement)
            curr_pos += len(matched_word)
        else:
            # if we didn't find any match at current position, we just copy the current character and move forward by one
            result_chars.append(text[curr_pos])
            curr_pos += 1

    return "".join(result_chars)

def main():
    compute_next_words()
    user_input = input("Enter a string: ")
    result = inflate(user_input)
    print(result)

if __name__ == "__main__":
    main()
