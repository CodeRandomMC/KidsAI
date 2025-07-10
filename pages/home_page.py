# pages/home_page.py
import gradio as gr

with gr.Blocks() as demo:
    # Welcome section
    gr.Markdown("# 🌟 Welcome to KidsAI Playground!", elem_classes=["page-title"])
    gr.Markdown("### Where imagination meets artificial intelligence! ✨", elem_classes=["page-subtitle"])
    
    # Introduction section
    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("""
            ## 🎨 What can you do here?
            
            **📖 Story Time Adventure**  
            Create magical stories! Choose your hero, pick a magical item, select an adventure world, and watch AI bring your imagination to life!
            
            **😂 Joke Factory**  
            Make super silly jokes! Pick two things and let AI create the funniest combinations that will make you giggle!
            
            **🧠 Fun Learning Adventures**  
            Turn learning into an adventure! Pick any topic and AI will create an exciting story to help you learn!
            """)
        
        with gr.Column(scale=1):
            gr.Markdown("""
            ## 🤖 About AI
            
            **What is AI?**  
            Artificial Intelligence (AI) is like having a super smart computer friend that can help create stories, jokes, and learn new things!
            
            **How does it work?**  
            You give AI your ideas (like picking a hero), and it uses its "brain" to create something amazing just for you!
            
            **You're the creative director!**  
            AI helps bring your ideas to life, but YOU are the one choosing what to create!
            """)
    
    # Fun facts section
    gr.Markdown("---")
    gr.Markdown("## 🎯 Fun AI Facts!")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
            **🚀 AI can help with:**
            - Writing stories
            - Creating jokes
            - Explaining science
            - Making learning fun
            - Answering questions
            """)
        
        with gr.Column():
            gr.Markdown("""
            **🎨 You bring the creativity:**
            - Choose the characters
            - Pick the settings
            - Decide what to learn
            - Guide the adventure
            - Make it YOUR story!
            """)
    
    # Getting started
    gr.Markdown("---")
    gr.Markdown("## 🚀 Ready to start your adventure?")
    gr.Markdown("Use the navigation menu at the top to explore different activities. Each one is designed to be fun, educational, and spark your creativity!")
    
    # Tips section
    with gr.Accordion("💡 Tips for the best experience", open=False):
        gr.Markdown("""
        - **Take your time** - There's no rush! Explore and have fun.
        - **Try different combinations** - Each choice creates a unique experience.
        - **Read your creations out loud** - Stories and jokes are even better when shared!
        - **Ask questions** - If you're curious about how something works, explore and discover!
        - **Be creative** - Your imagination is the most important ingredient!
        """)

if __name__ == "__main__":
    demo.launch()
