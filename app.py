# app.py
import gradio as gr

# Import page modules
import pages.home_page as home_page
import pages.story_page as story_page
import pages.joke_page as joke_page
import pages.learn_page as learn_page

# Import theme and header
from ui.theme import kids_theme, multipage_css
from ui.header import create_header

# --- Build the Multipage Gradio App ---
with gr.Blocks(theme=kids_theme, title="KidsAI Playground", css=multipage_css) as demo:
    
    # Create the persistent header on the home page
    create_header()
    
    # Render the home page content
    home_page.demo.render()

# Add separate pages using routes
with demo.route("📖 Story Time", "/story"):
    create_header()  # Header on each page
    story_page.demo.render()

with demo.route("😂 Joke Factory", "/jokes"):
    create_header()  # Header on each page  
    joke_page.demo.render()

with demo.route("🧠 Fun Learning", "/learn"):
    create_header()  # Header on each page
    learn_page.demo.render()

# --- Launch the App ---
if __name__ == "__main__":
    demo.launch()