import openai
import requests
from tkinter import messagebox

def interact_with_chatgpt(prompt, model, max_tokens, temperature, role):
    messages = [
        {"role": "system", "content": f"You are a {role}."},
        {"role": "user", "content": prompt}
    ]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}",
    }

    response = requests.post(
        f"https://api.openai.com/v1/chat/completions",
        headers=headers,
        json={
            "model": model,
            "messages": messages,
            "max_tokens": int(max_tokens),
            "temperature": temperature,
        },
    )
    if response.status_code != 200:
        error_message = response.json().get('error', {}).get('message', 'Unknown error')
        messagebox.showerror("Error", error_message)
        return None
    # Print the response text for debugging
    response_data = response.json()
    print("ID:", response_data['id'])
    print("Model:", response_data['model'])
    print("Usage:", response_data['usage']) 
    
    response.raise_for_status()
    return response.json()
