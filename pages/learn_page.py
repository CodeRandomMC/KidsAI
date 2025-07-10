# pages/learn_page.py
import gradio as gr
from ui.learn_tab import create_learn_tab

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Fun Learning Adventures", elem_classes=["page-title"])
    gr.Markdown("Turn any topic into an exciting adventure! Learn through amazing stories.", elem_classes=["page-subtitle"])
    create_learn_tab()

if __name__ == "__main__":
    demo.launch()
