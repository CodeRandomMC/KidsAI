# ui/header.py
import gradio as gr

def create_header():
    """Creates the header section for the KidsAI app with parental controls."""
    with gr.Row():
        with gr.Column(scale=4):
            gr.Markdown(
                """
                # 🧸 KidsAI: The AI Playground
                A safe and fun place for kids to create and learn!
                """,
                elem_id="app-header"
            )
        with gr.Column(scale=1, min_width=150):
            with gr.Accordion("👨‍👩‍👧‍👦 Parent Mode", open=False):
                parent_mode = gr.Checkbox(label="Enable Parent Guidance", value=False)
                gr.Markdown("When enabled, provides additional context and vocabulary help.")
                
    return parent_mode