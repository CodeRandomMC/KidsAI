# app.py
import gradio as gr

# Import UI modules and logic
from ui.theme import kids_theme
from ui.header import create_header
from ui.story_tab import create_story_tab
from ui.joke_tab import create_joke_tab
from ui.learn_tab import create_learn_tab
from logic.llm_interface import safe_generate_lesson

# --- Build the Gradio App ---
with gr.Blocks(theme=kids_theme, title="KidsAI Playground") as demo:
    
    # 1. Create the persistent header
    create_header()
    
    # 2. Create the main navigation tabs
    with gr.Tabs():
        
        # Story Generator Tab
        with gr.TabItem("📖 Story Time", id="story_tab"):
            create_story_tab()  # Now self-contained

        # Joke Factory Tab
        with gr.TabItem("😂 Joke Factory", id="joke_tab"):
            create_joke_tab()  # Now self-contained
            
        # Fun Learning Tab
        with gr.TabItem("🧠 Fun Learning", id="learn_tab"):
            learn_btn, learn_inputs, learn_outputs = create_learn_tab()

    # 3. Connect the backend logic to the UI (only for learn tab)
    # Note: Story and Joke tabs are now self-contained
    
    learn_btn.click(
        fn=safe_generate_lesson,
        inputs=learn_inputs,
        outputs=learn_outputs
    )

# --- Launch the App ---
if __name__ == "__main__":
    demo.launch()