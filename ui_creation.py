import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from ui_actions import on_input_text_keypress
from themes import themes
from roles import roles


def create_settings_panel(parent):
    settings_panel = tk.Frame(parent, bg="#2b2b2b", bd=2, relief=tk.SOLID)
    
    settings_label = tk.Label(settings_panel, text="Settings", font=("Arial", 14), fg="white", bg="#2b2b2b")
    settings_label.pack(side=tk.TOP, padx=10, pady=10)

    # Add a label and combobox for the model
    model_label = tk.Label(settings_panel, text="Model", font=("Arial", 12), fg="white", bg="#2b2b2b")
    model_label.pack(anchor=tk.W, padx=10, pady=5)

    model_combobox = ttk.Combobox(settings_panel, values=[
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-0301",
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k",
        "gpt-3.5-turbo-16k-0613"
    ], state="readonly")
    model_combobox.set("gpt-3.5-turbo")
    model_combobox.pack(anchor=tk.W, padx=10, pady=5)

    max_tokens_label = tk.Label(settings_panel, text="Max Tokens", font=("Arial", 12), fg="white", bg="#2b2b2b")
    max_tokens_label.pack(anchor=tk.W, padx=10, pady=5)

    max_tokens_scale = tk.Scale(settings_panel, from_=1, to=4000, orient=tk.HORIZONTAL, fg="white", bg="#2b2b2b", sliderrelief=tk.FLAT, activebackground="#3b3b3b")
    max_tokens_scale.set(4000)
    max_tokens_scale.pack(anchor=tk.W, padx=10, pady=5)

    temperature_label = tk.Label(settings_panel, text="Temperature", font=("Arial", 12), fg="white", bg="#2b2b2b")
    temperature_label.pack(anchor=tk.W, padx=10, pady=5)

    temperature_scale = tk.Scale(settings_panel, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, fg="white", bg="#2b2b2b", sliderrelief=tk.FLAT, activebackground="#3b3b3b")
    temperature_scale.set(0.7)
    temperature_scale.pack(anchor=tk.W, padx=10, pady=5)

    roles_label = tk.Label(settings_panel, text="Role", font=("Arial", 12), fg="white", bg="#2b2b2b")
    roles_label.pack(anchor=tk.W, padx=10, pady=5)

    roles_combobox = ttk.Combobox(settings_panel, values=[
        "helpful_assistant", "python_programmer", "web_developer", "data_scientist", "machine_learning_engineer", "software_architect", "cybersecurity_expert", "network_engineer", "database_administrator", "technical_writer", "project_manager", "qa_engineer", "travel_planner", "fitness_advisor", "nutrition_expert", "personal_finance_consultant", "relationship_advisor", "movie_recommendation_engine", "book_suggestion_engine", "shopping_assistant", "career_advisor", "language_tutor", "software_engineer_assistant"
    ], state="readonly")
    roles_combobox.set("helpful_assistant")
    roles_combobox.pack(anchor=tk.W, padx=10, pady=5)

    def update_max_tokens_scale(*args):
        selected_model = model_combobox.get()
        if selected_model in ["gpt-3.5-turbo-16k-0613", "gpt-3.5-turbo-16k"]:
            max_tokens_scale.config(to=16000)
            max_tokens_scale.set(16000)
        else:
            max_tokens_scale.config(to=4000)
            max_tokens_scale.set(4000)

    model_combobox.bind("<<ComboboxSelected>>", update_max_tokens_scale)

    return settings_panel, model_combobox, max_tokens_scale, temperature_scale, roles_combobox


def create_right_frame(parent):
    # function content here
        right_frame = tk.Frame(parent, bg="#2b2b2b")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
        output_label = tk.Label(right_frame, text="ChatGPT Response", font=("Arial", 12), fg="white", bg="#2b2b2b")
        output_label.pack(side=tk.TOP, padx=10, pady=10)
    
        output_text = ScrolledText(right_frame, wrap=tk.WORD, font=("Arial", 12), fg="white", bg="#4b4b4b", insertbackground="white", state="disabled")

        output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
        # Configure the "user_input" tag for different color and font
        output_text.tag_configure("user_input", foreground="cyan", font=("Arial", 12, "bold"))
    
        return right_frame, output_text
def create_left_frame(parent, output_text):
    # function content here
    left_frame = tk.Frame(parent, bg="#2b2b2b")
    left_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)

    input_label = tk.Label(left_frame, text="Your Input", font=("Arial", 12), fg="white", bg="#2b2b2b")
    input_label.pack(side=tk.TOP, padx=10, pady=10)

    input_text = tk.scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, font=("Arial", 12), height=6, fg="white", bg="#4b4b4b", insertbackground="white")
    input_text.pack(fill=tk.X, expand=False, padx=10, pady=0)
    input_text.bind("<KeyPress>", lambda event: on_input_text_keypress(event, input_text, output_text, model_combobox, max_tokens_scale, temperature_scale, roles_combobox))

    settings_panel, model_combobox, max_tokens_scale, temperature_scale, roles_combobox = create_settings_panel(left_frame, output_text)
    settings_panel.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    send_button = tk.Button(left_frame, text="Send", command=lambda: on_send_button_click(input_text, output_text, model_combobox, max_tokens_scale, temperature_scale, roles_combobox), bg="#3b3b3b", fg="white", activebackground="#5b5b5b", activeforeground="white")
    send_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    return left_frame, input_text


def create_ui():
    def apply_theme(theme):
        window.configure(bg=theme["background"])
        main_frame.configure(bg=theme["background"])
        input_text.configure(
            bg=theme["input_background"],
            fg=theme["input_text_color"]
        )
        output_text.configure(
            bg=theme["output_background"],
            fg=theme["output_text_color"]
        )
        # Add more widget configuration for other elements

    def on_role_change(event):
        selected_role = roles_combobox.get()
        if selected_role in themes:
            theme = themes[selected_role]
            apply_theme(theme)

    window = tk.Tk()
    window.title("ChatGPT Developer's Hub")
    window.state('zoomed')

    main_frame = tk.Frame(window, bg="#2b2b2b")
    main_frame.pack(fill=tk.BOTH, expand=True)

    right_frame, output_text = create_right_frame(main_frame)
    left_frame, input_text = create_left_frame(main_frame, output_text)
    settings_panel, model_combobox, max_tokens_scale, temperature_scale, roles_combobox = create_settings_panel(left_frame, output_text)

    roles_combobox["values"] = tuple(roles)
    roles_combobox.bind("<<ComboboxSelected>>", on_role_change)

    window.mainloop()

