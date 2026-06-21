def generate_flashcards_from_notes(notes):

    flashcards = []

    sentences = notes.split(".")

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence.split()) > 4:

            words = sentence.split()

            question = f"What is meant by: {' '.join(words[:4])}...?"

            answer = sentence

            flashcards.append({
                "question": question,
                "answer": answer
            })

    return flashcards[:10]
