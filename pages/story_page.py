# pages/story_page.py
import gradio as gr
from ui.story_tab import create_story_tab

with gr.Blocks() as demo:
    gr.Markdown("# 📖 Story Time Adventure", elem_classes=["page-title"])
    gr.Markdown("Create magical stories with AI! Choose your hero, magical item, and adventure world.", elem_classes=["page-subtitle"])
    create_story_tab()

if __name__ == "__main__":
    demo.launch()
