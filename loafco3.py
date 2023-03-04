import openai
import tkinter as tk
from datetime import datetime
import configparser
import os
import sys

# Set up the API key
config = configparser.ConfigParser()

if os.path.exists("keyconf.ini"):
    config.read("keyconf.ini")
    api_key = config["API_KEY"]["key"]
else:
    api_key = input("Please enter your OpenAI API key: ")
    config["API_KEY"] = {"key": api_key}
    with open("keyconf.ini", "w") as f:
        config.write(f)

openai.api_key = api_key

# Define the prompt for the chatbot
prompt = [{"role": "system", "content": "" }]

# Create an empty chat history list
chat_history = []


# Create a tkinter window with an entry box and a chat display
window = tk.Tk()
window.title("ChatGPT")
window.geometry("1280x800")






chat_display = tk.Text(window, state=tk.DISABLED, wrap=tk.WORD, bg="#EAEFF7")
chat_display.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(window, command=chat_display.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
chat_display.config(yscrollcommand=scrollbar.set)

# Add the chat history to the chat display
if os.path.exists("Mar3LogStart.txt"):
    with open("Mar3LogStart.txt", "r") as f:
        log_text = f.read()
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, log_text)
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

def get_response():
    # Get the user input from the entry box
    user_input = entry.get()

    # Generate a response using the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": user_input }],
        n=1,
        temperature=1.1,
    )

 #   # Check if the response object has choices and text attributes
 #   if len(response.choices) > 0 and hasattr(response.choices[0], "text"):
 #       # Get the response text from the API
 #       response_text = response.choices[0].text.strip()
  #  else:
 #       response_text = "Sorry, I could not generate a response at this time."
    response_text = response ['choices'][0]['message']['content']
    # Add the conversation to the chat history
    chat_history.append(("User", user_input))
    chat_history.append(("Chatbot", response_text))

    # Clear the entry box and update the chat display
    entry.delete(0, tk.END)
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_display.insert(tk.END, "Chatbot: " + response_text + "\n\n", "bot")
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

    # Configure text tags for prompt and response
    chat_display.tag_config("user", foreground="blue")
    chat_display.tag_config("bot", foreground="green")

entry = tk.Entry(window, width=60)
entry.pack(side=tk.TOP, pady=10, padx=10, anchor='w')
entry.config(font=("Courier", 14), justify='left')

# Bind the entry box to the "Return" key to generate a response
entry.bind("<Return>", lambda event: get_response())

send_button = tk.Button(window, text="Send", command=get_response)
send_button.pack(side=tk.LEFT, padx=10, pady=10)
# Create a function to save chat history to log file
def save_chat_history():
    with open("Mar3LogStart.txt", "a") as f:
        f.write(f"Log ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for item in chat_history:
            f.write(f"{item[0]}: {item[1]}\n")

# Create a restart button that restarts the program
#def restart_program():
#    save_chat_history()
 #   window.destroy()
#    os.execv('wingpt.py', sys.argv)

#restart_button = tk.Button(window, text="Restart", command=restart_program)
#restart_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.SW)

# Create a function to close the program and save chat history to log file
def close_program():
  #  save_chat_history()
    window.destroy()

close_button = tk.Button(window, text="Close", command=close_program)
close_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.SW)

# Start the tkinter event loop
window.mainloop()

# Migrate log file to new version
try:
    os.system('python migrate.py')
except:
    pass # Ignore errors in migration script

# Close the program and save chat history to log file
save_chat_history()
print("Saved")
sys.exit()
