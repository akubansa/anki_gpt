import os
import openai
import pyperclip

# Set up OpenAI API key
#openai.api_key = os.environ["OPENAI_API_KEY"]
os.environ["HUGGINGFACEHUB_API_TOKEN"] 

#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

#------------wgranie klucza------------
#echo "export OPENAI_API_KEY='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'" >> ~/.zshrc
#source ~/.zshrc
#echo $OPENAI_API_KEY

#------------error urllib3-------------
#pip install urllib3==1.26.16  

# Get content from clipboard
clipboard_content = pyperclip.paste()
#clipboard_content = 'consider'
# Create a conversation with ChatGPT
messages = [
    {"role": "system", "content": "you are an English teacher, student Polish. Provide example sentence for using word. State the question::answer in one line"},
    {"role": "user", "content": f"Create anki flashcards with the following text using a format like line question::answer, next line question::answer. state the question;answer in one line, etc... word:{clipboard_content}."}
]
#Utwórz fiszki anki z następującym tekstem tlumacac go na jezyk polski, używając formatu takiego jak pytanie;odpowiedź w następnym wierszu pytanie;odpowiedź itp.{clipboard_content}."}


response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0.7,
    max_tokens=2000
)

generated_flashcards = response["choices"][0]["message"]["content"]

# Save flashcards to a file
with open("/Users/kubansa/project/anki_gpt/flashcards.txt", "a") as f:
    f.write(generated_flashcards)

print("Flashcards saved to 'flashcards.txt'")


