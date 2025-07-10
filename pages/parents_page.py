# pages/parents_page.py
import gradio as gr

with gr.Blocks() as demo:
    # Header section
    gr.Markdown("# 👨‍👩‍👧‍👦 For Parents & Guardians", elem_classes=["page-title"])
    gr.Markdown("### Understanding the Mission Behind KidsAI", elem_classes=["page-subtitle"])
    
    # Mission statement
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
            ## 🎯 Why I Built KidsAI
            
            As we stand at the threshold of an AI-driven future, I believe we have a choice: we can either prepare our children to understand and harness this technology responsibly, or we can leave them to discover it without guidance.
            
            **KidsAI isn't about replacing creativity—it's about amplifying it.**
            
            When your child uses KidsAI, they aren't becoming passive consumers of AI-generated content. They are becoming **creative directors**, making choices, guiding narratives, and learning that technology is a tool that responds to *their* imagination.
            """)
    
    # Core philosophy section
    gr.Markdown("---")
    gr.Markdown("## 🧭 The Philosophy: Creative Partnership, Not Replacement")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("""
            ### 🎨 Your Child is the Artist
            
            Think of AI like a sophisticated paintbrush. The brush doesn't create the painting—the artist does. Similarly, when your child selects a "Brave Knight," "Magic Boots," and "Enchanted Forest," **they** are crafting the creative vision. AI simply helps bring that vision to life.
            
            **The creativity is 100% theirs.**
            """)
        
        with gr.Column(scale=1):
            gr.Markdown("""
            ### 🛡️ Safety by Design
            
            KidsAI uses a "promptless" interface—no free text input—making harmful content impossible by design. Every output goes through a dedicated safety review system before reaching your child.
            
            **Trust through engineering, not just promises.**
            """)
    
    # The "why now" section
    gr.Markdown("---")
    gr.Markdown("## 🌍 Why This Matters Now")
    
    gr.Markdown("""
    ### The Reality of Our Children's Future
    
    AI will be as fundamental to your child's world as the internet is today. Just as we taught digital literacy, we now need to foster **AI literacy**—but safely, positively, and early.
    
    **The goal isn't to create AI experts; it's to create confident, creative thinkers who see technology as a tool for expression, not a mysterious black box.**
    """)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
            ### 🎭 The Magic Moment
            
            When a 6-year-old presses a few buttons and generates a unique story that never existed before—a story that is truly *theirs*—they experience a powerful "I made this!" moment.
            
            This isn't about consuming technology; it's about **commanding it to serve their imagination**.
            """)
        
        with gr.Column():
            gr.Markdown("""
            ### 🌱 Building Creative Confidence
            
            In a world where AI can generate content instantly, the most valuable skill isn't technical proficiency—it's **creative vision**. KidsAI nurtures this by putting your child in the director's chair.
            """)
    
    # Addressing concerns
    gr.Markdown("---")
    gr.Markdown("## 🤔 Addressing Common Concerns")
    
    with gr.Accordion("\"Won't this make my child dependent on AI for creativity?\"", open=False):
        gr.Markdown("""
        **Quite the opposite.** KidsAI teaches children that AI is a *tool that responds to their choices*. They learn to be the creative director, making decisions about characters, settings, and outcomes. This builds creative confidence and decision-making skills.
        
        Compare this to passively consuming pre-made content. With KidsAI, your child is actively shaping the narrative.
        """)
    
    with gr.Accordion("\"Is my child too young to understand AI?\"", open=False):
        gr.Markdown("""
        Children are natural learners and surprisingly adaptable to new technologies. KidsAI introduces AI concepts through play and creation, not complex technical explanations.
        
        **They don't need to understand the mechanics of AI any more than they need to understand combustion engines to benefit from cars.** They need to understand that it's a tool that responds to their creativity.
        """)
    
    with gr.Accordion("\"What about screen time and digital wellness?\"", open=False):
        gr.Markdown("""
        KidsAI is designed for **quality over quantity**. Sessions are naturally brief (5-10 minutes) and focused on creative output rather than endless scrolling.
        
        **The goal is inspiration, not addiction.** Children create something, enjoy it, and often want to share it—then they move on to other activities.
        """)
    
    # The bigger picture
    gr.Markdown("---")
    gr.Markdown("## 🚀 The Bigger Picture: Foundation for Life")
    
    gr.Markdown("""
    ### Building Tomorrow's Thinkers
    
    KidsAI is my proof-of-concept for a larger mission: building AI that is truly worthy of a child's trust. The safety architecture, creative partnership model, and educational approach demonstrated here lay the groundwork for more sophisticated AI companions as children grow.
    
    **This isn't just about stories and jokes—it's about establishing a healthy, empowering relationship with AI technology from day one.**
    """)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
            ### 🌟 What Your Child Learns
            
            - **Decision-making**: Every choice shapes the outcome
            - **Creative ownership**: Their ideas drive the experience  
            - **Technology confidence**: AI responds to *their* commands
            - **Critical thinking**: Understanding cause and effect
            - **Communication**: Expressing ideas through selections
            """)
        
        with gr.Column():
            gr.Markdown("""
            ### 🎯 Long-term Benefits
            
            - Confident interaction with future AI tools
            - Understanding of human-AI collaboration
            - Strong creative problem-solving skills
            - Healthy relationship with technology
            - Reduced fear or mystification of AI
            """)
    
    # Important disclaimer and guidance
    gr.Markdown("---")
    
    with gr.Row():
        with gr.Column():
            gr.HTML("""
            <div style="background: linear-gradient(135deg, #fef3c7 0%, #fcd34d 100%); 
                        border-left: 6px solid #f59e0b; padding: 25px; border-radius: 12px; 
                        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.2);">
                <h3 style="margin-top: 0; color: #92400e;">
                    ⚠️ Important: We Highly Recommend Parental Guidance
                </h3>
                <p style="color: #92400e; font-size: 16px; line-height: 1.6; margin-bottom: 0;">
                    <strong>KidsAI is designed to be explored together.</strong> Children are naturally more 
                    engaged and learn better when sharing experiences with trusted adults. Your presence 
                    transforms a digital activity into a bonding moment and learning opportunity.
                </p>
            </div>
            """)
    
    # Call to action
    gr.Markdown("## 💫 Ready to Explore Together?")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
            ### 🎯 The Parent-Child Experience
            
            **Sit with your child during their KidsAI sessions.** Your engagement amplifies their excitement and learning:
            
            - **Ask about their choices**: "Why did you pick the brave knight? What do you think will happen?"
            - **Celebrate their creativity**: "Wow! YOU created this amazing story!"
            - **Make connections**: "This reminds me of that book we read together..."
            - **Share the wonder**: You might be surprised by the creative combinations they discover!
            """)
        
        with gr.Column():
            gr.Markdown("""
            ### 👨‍👩‍👧‍👦 You Might Create Something Amazing Too!
            
            Don't be surprised if you find yourself just as fascinated by the creative possibilities. Many parents discover that:
            
            - **You become co-creators** in the storytelling process
            - **Your own creativity is sparked** by your child's unique choices
            - **You gain insights** into how your child thinks and imagines
            - **You create shared memories** around these collaborative stories
            
            **This isn't just screen time—it's creative time together.**
            """)
    
    gr.Markdown("""
    ### 🌟 Making It Easy to Get Started
    
    **First Session Tips:**
    1. **Start together**: Explore the interface with your child in the first session
    2. **Let them lead**: Allow your child to make the creative choices while you provide encouragement
    3. **Read aloud**: Take turns reading the generated stories together
    4. **Ask open questions**: "What would you change?" "What happens next?"
    5. **Save or share**: Consider printing favorite stories or sharing them with family
    
    **This is their tool, their creativity, their future—guided by your wisdom and enhanced by your presence.**
    """)
    
    # Technical transparency
    with gr.Accordion("🔧 Technical Details for Curious Parents", open=False):
        gr.Markdown("""
        **Privacy**: KidsAI is completely stateless—no data is stored about your child's interactions.
        
        **Safety Pipeline**: Every AI output is reviewed by a dedicated safety system before display.
        
        **No Prompt Injection**: The button-based interface makes malicious inputs structurally impossible.
        
        **Content Framing**: All stories are clearly presented as "make-believe" to prevent confusion with reality.
        
        **Transparent Operation**: The system is designed to be understood, not mysterious.
        """)

if __name__ == "__main__":
    demo.launch()
