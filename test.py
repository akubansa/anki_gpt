with open("flashcards.txt") as file:
            for row in file.readlines()[1:]:
                question, answer =  (row.split("::")[0:])
                notes = "('" + question + "'," + "'"+answer + "')"
                with open("/Users/kubansa/project/anki_gpt/flashcards2.txt", "a") as f:
                    f.write(notes)

            