# ─────────────────────────────────────────
# Task 1 – String & Collections
# ─────────────────────────────────────────
def most_common_word(text: str, stopwords: set[str]) -> str | None:
    """
    Return the most frequently occurring word in text,
    ignoring any words in stopwords. Case-insensitive.
    Returns None if no eligible words exist.
    """
    # 1. Normalize and split text into words
    # 2. Filter out stopwords (if provided)
    # 3. Count word frequencies
    # 4. Return the most common word, or None if empty

    words = text.split(" ")
    lowercase_stopwords = [stopword.lower() for stopword in stopwords]
    word_count = {}

    for word in words:
        word = word.lower()
        if word not in lowercase_stopwords:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    sorted_word_list = list(sorted_word_count.keys())

    if (len(sorted_word_list) > 0):
        return sorted_word_list[0]
    else:
        return None

most_common_word("hello My NAME is Ian helLO HELLO is my my hello", ["is", "MY"])
