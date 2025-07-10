# ui/joke_tab.py
import gradio as gr
from logic.llm_interface import JOKE_SUBJECTS_1, JOKE_SUBJECTS_2

def create_joke_tab():
    """Creates the UI for the Joke Factory tab."""
    gr.Markdown("## 😂 Welcome to the Joke Factory!")
    
    with gr.Row(equal_height=False):
        with gr.Column(scale=1):
            subject1 = gr.Radio(label="What do you cross...", choices=JOKE_SUBJECTS_1, value=JOKE_SUBJECTS_1[0])
        with gr.Column(scale=1):
            subject2 = gr.Radio(label="...with a...", choices=JOKE_SUBJECTS_2, value=JOKE_SUBJECTS_2[0])

    btn = gr.Button("😂 Tell Me The Joke!", variant="primary")
    output_joke = gr.Textbox(label="Here's a funny!", interactive=False, lines=3)
    
    inputs = [subject1, subject2]
    outputs = [output_joke]
    
    return btn, inputs, outputs