# ui/learn_tab.py
import gradio as gr
from logic.llm_interface import LEARN_SUBJECTS, LEARN_THEMES

def create_learn_tab():
    """Creates the UI for the Fun Learning tab."""
    gr.Markdown("## 🧠 Let's make learning an adventure!")

    with gr.Row():
        with gr.Column():
            subject = gr.Dropdown(label="What do you want to learn about?", choices=LEARN_SUBJECTS, value=LEARN_SUBJECTS[0])
            theme = gr.Dropdown(label="Choose a fun theme!", choices=LEARN_THEMES, value=LEARN_THEMES[0])
            age = gr.Slider(label="How old are you?", minimum=4, maximum=10, step=1, value=6)
            
    btn = gr.Button("🚀 Let's Learn!", variant="primary")
    output_lesson = gr.Markdown(value="*Your fun lesson will appear here...*")

    inputs = [subject, theme, age]
    outputs = [output_lesson]
    
    return btn, inputs, outputs