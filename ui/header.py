# ui/header.py
import gradio as gr

def create_header():
    """Creates the header section for the KidsAI app."""
    with gr.Row():
        gr.Markdown(
            """
            # 🧸 KidsAI: The AI Playground
            A safe and fun place for kids to create and learn!
            """,
            elem_id="app-header" # For potential CSS styling
        )