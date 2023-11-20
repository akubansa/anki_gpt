import os
import openai
import pyperclip
from dotenv import load_dotenv
# pip install python-dotenv==0.21.0

# Set up OpenAI API key
load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
#openai.api_key = os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


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
    f.write(clipboard_content)
    f.write("\n")


with open("/Users/kubansa/project/anki_gpt/flashcards.txt", "a") as f:
    f.write(generated_flashcards)
    f.write("\n")
    f.write("\n")

print("Flashcards saved to 'flashcards.txt'")


