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
    
    # Parent/Guardian call to action
    gr.Markdown("---")
    
    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("""
            ## 👨‍👩‍👧‍👦 A Message for Parents & Guardians
            
            **Your child isn't just "using AI"—they're learning to be creative directors of cutting-edge technology.**
            
            When children interact with KidsAI, they make every creative decision. They choose the hero, the magical item, the setting. AI simply helps bring *their* vision to life—like a sophisticated paintbrush responding to an artist's guidance.
            
            **This is about empowerment, not replacement.** Your child is developing confidence with technology that will be fundamental to their future, while building creative problem-solving skills that will serve them for life.
            
            **💡 Best experienced together!** Children learn better and are more engaged when exploring new technology with trusted adults. You might discover your own creativity sparked by their unique imagination!
            """)
        
        with gr.Column(scale=1):
            gr.HTML("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 25px; border-radius: 15px; text-align: center; color: white; 
                        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);">
                <h3 style="margin-top: 0; color: white;">🌟 Learn More About Our Mission</h3>
                <p style="font-size: 16px; line-height: 1.5; margin: 15px 0;">
                    Discover why KidsAI is designed as a creative partnership tool, 
                    plus tips for the best parent-child experience.
                </p>
                <a href="/parents" style="display: inline-block; background: white; color: #667eea; 
                   padding: 12px 24px; border-radius: 25px; text-decoration: none; 
                   font-weight: bold; margin-top: 10px; transition: transform 0.2s;"
                   onmouseover="this.style.transform='scale(1.05)'" 
                   onmouseout="this.style.transform='scale(1)'">
                    👨‍👩‍👧‍👦 For Parents & Guardians
                </a>
            </div>
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
