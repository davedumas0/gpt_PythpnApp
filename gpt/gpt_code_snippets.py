import pygments
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def get_code_snippet(code, language):
    lexer = get_lexer_by_name(language)
    formatter = HtmlFormatter(linenos=True)
    return highlight(code, lexer, formatter)

def display_code_snippet(code, language):
    highlighted_code = get_code_snippet(code, language)
    print(highlighted_code)

def save_code_snippet_to_file(code, language, output_file):
    highlighted_code = get_code_snippet(code, language)
    with open(output_file, "w") as f:
        f.write(highlighted_code)
