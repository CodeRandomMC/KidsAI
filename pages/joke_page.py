# pages/joke_page.py
import gradio as gr
from ui.joke_tab import create_joke_tab

with gr.Blocks() as demo:
    gr.Markdown("# 😂 Joke Factory", elem_classes=["page-title"])
    gr.Markdown("Let's make super silly jokes together! Pick two things and watch the magic happen.", elem_classes=["page-subtitle"])
    create_joke_tab()

if __name__ == "__main__":
    demo.launch()
