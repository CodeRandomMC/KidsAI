# app.py
import gradio as gr

# Import page modules
import pages.home_page as home_page
import pages.story_page as story_page
import pages.joke_page as joke_page
import pages.learn_page as learn_page
import pages.parents_page as parents_page

# Import theme
from ui.theme import kids_theme, multipage_css

# --- Build the Multipage Gradio App ---
with gr.Blocks(theme=kids_theme, title="KidsAI Playground", css=multipage_css) as demo:
    # Render the home page content in the default Home tab
    home_page.demo.render()

# Add separate pages using routes
with demo.route("📖 Story Time", "/story"):
    story_page.demo.render()

with demo.route("😂 Joke Factory", "/jokes"):
    joke_page.demo.render()

with demo.route("🧠 Fun Learning", "/learn"):
    learn_page.demo.render()

with demo.route("🫂 Parents/Guardians", "/parents"):
    parents_page.demo.render()

# --- Launch the App ---
if __name__ == "__main__":
    demo.launch()