from dependencies import check_and_install_dependencies
from api_config import api_key, openai
from api_functions import interact_with_chatgpt
from ui_actions import on_send_button_click, on_input_text_keypress
from ui_creation import create_ui

if __name__ == "__main__":
    create_ui()
