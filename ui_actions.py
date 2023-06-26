
import tkinter as tk
from api_functions import interact_with_chatgpt
from ui_creation import apply_theme
from themes import themes

def on_send_button_click(input_text, output_text, model_combobox, max_tokens_scale, temperature_scale, roles_combobox):

    # function content here
    prompt = input_text.get(1.0, tk.END).strip()
    model = model_combobox.get()  # Get the selected model
        # Adjust max token limit for specific models
    if model in ["gpt-3.5-turbo-16k-0613", "gpt-3.5-turbo-16k"]:
        max_tokens = 16000
    else:
     max_tokens = max_tokens_scale.get()
     temperature = temperature_scale.get()
     role = roles_combobox.get()
     theme = themes[role]
    apply_theme(theme)
    response_text = interact_with_chatgpt(prompt, model, max_tokens, temperature, role)
    response_message = response_text['choices'][0]['message']['content']

    output_text.configure(state='normal')
    output_text.insert(tk.END, f"\n> {prompt}", "user_input")
    output_text.insert(tk.END, f"\n{response_message}")
    output_text.configure(state='disabled')

    input_text.delete(1.0, tk.END)


def on_input_text_keypress(event, input_text, output_text, model_combobox, max_tokens_scale, temperature_scale, roles_combobox):
    # function content here
    if event.state == 1 << 0 and event.keysym == "Return": # Shift+Return
        input_text.insert(tk.END, "\n")
    elif event.keysym == "Return": # Return
        on_send_button_click(input_text, output_text, model_combobox, max_tokens_scale, temperature_scale, roles_combobox)