
def vowel_counter(sentence):
    result = {}
    for vowel in "aeiou":
        result[vowel]= sentence.lower().count(vowel)
    return result

if __name__== "__main__":
    msg = "this is a test "
    print(vowel_counter(msg))

