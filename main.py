
def analyze_text(text):
    words = text.split()
    characters = len(text)
    characters_without_spaces = len(text.replace(" ", ""))
    sentences = sum(text.count(mark) for mark in ".!?")

    return {
        "words": len(words),
        "characters": characters,
        "characters_without_spaces": characters_without_spaces,
        "sentences": sentences
    }


def main():
    print("=" * 35)
    print("         TEXT ANALYZER")
    print("=" * 35)

    text = input("Enter your text: ")

    if not text.strip():
        print("Please enter some text.")
        return

    results = analyze_text(text)

    print("\n----- ANALYSIS RESULTS -----")
    print(f"Words: {results['words']}")
    print(f"Characters: {results['characters']}")
    print(
        "Characters without spaces: "
        f"{results['characters_without_spaces']}"
    )
    print(f"Sentences: {results['sentences']}")

    search_word = input("\nEnter a word to search for: ").strip()

    if search_word:
        occurrences = text.lower().count(search_word.lower())
        print(f"Occurrences of '{search_word}': {occurrences}")

    print("----------------------------")
    print("Analysis complete!")


if __name__ == "__main__":
    main()
