# ─────────────────────────────────────────
# Task 1 – String & Collections
# ─────────────────────────────────────────
def most_common_word(text: str, stopwords: set[str]) -> str | None:
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
