def analyze_text(text):
    words = text.split()

    num_words = len(words)
    num_characters = len(text)
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    num_paragraphs = len([p for p in text.split('\n') if p.strip() != ''])

    word_freq = {}

    for word in words:
        word = word.lower().strip('.,!?()[]{}"\'')
        word_freq[word] = word_freq.get(word, 0) + 1

    most_common_word = max(word_freq, key=word_freq.get) if word_freq else None
    longest_word = max(words, key=len) if words else None

    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0

    return {
        "words": num_words,
        "characters": num_characters,
        "sentences": num_sentences,
        "paragraphs": num_paragraphs,
        "most_common_word": most_common_word,
        "longest_word": longest_word,
        "avg_word_length": round(avg_word_length, 2)
    }


if __name__ == "__main__":
    print("\n--- Word Counter & Text Analyzer ---\n")
    text = input("Enter your text:\n")

    result = analyze_text(text)

    print("\n--- Analysis Report ---")
    for key, value in result.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
