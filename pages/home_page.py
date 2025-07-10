# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (c) 2025 Jack Pollard

# pages/home_page.py
import gradio as gr
import os

def create_welcome_animation():
    return """
    <div class="welcome-animation">
        <div class="welcome-text">
            <h1>🌟 Welcome to KidsAI!</h1>
            <p>Your creative adventure begins now!</p>
        </div>
    </div>
    <style>
    .welcome-animation {
        background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 25px rgba(14, 165, 233, 0.5);
        margin-bottom: 30px;
        animation: welcome-fade 1.5s ease-out forwards;
    }
    .welcome-text h1 {
        font-size: 2.5em;
        margin-bottom: 10px;
        animation: text-pop 1s ease-out 0.5s forwards;
        opacity: 0;
        transform: translateY(20px);
    }
    .welcome-text p {
        font-size: 1.3em;
        opacity: 0;
        animation: text-pop 1s ease-out 1s forwards;
        transform: translateY(20px);
    }
    @keyframes welcome-fade {
        0% { transform: scale(0.9); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    @keyframes text-pop {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
    """

# Check if this is the first time the user is visiting
def is_first_visit():
    visit_flag = os.path.join(os.path.dirname(__file__), "..", ".user_visited")
    first_visit = not os.path.exists(visit_flag)
    if first_visit:
        # Create the flag file to track that user has visited
        with open(visit_flag, "w") as f:
            f.write("visited")
    return first_visit

with gr.Blocks() as demo:
    # First-time visitor welcome animation
    first_time = is_first_visit()
    welcome_animation = gr.HTML(create_welcome_animation() if first_time else "", visible=first_time)
    
    # Welcome section
    gr.Markdown("# 🌟 Welcome to KidsAI Playground!", elem_classes=["page-title"])
    gr.Markdown("### Where imagination meets artificial intelligence! ✨", elem_classes=["page-subtitle"])
    
    # Feature Showcase with visual cards
    gr.HTML("""
    <div class="feature-showcase">
        <div class="feature-card story-card">
            <div class="feature-icon">📖</div>
            <h3>Story Time Adventure</h3>
            <p>Create magical stories with heroes, items, and fantastic worlds!</p>
            <a href="/story" class="feature-button">Start Creating</a>
        </div>
        
        <div class="feature-card joke-card">
            <div class="feature-icon">😂</div>
            <h3>Joke Factory</h3>
            <p>Mix funny ingredients to create hilarious jokes that will make you laugh!</p>
            <a href="/jokes" class="feature-button">Get Silly</a>
        </div>
        
        <div class="feature-card learn-card">
            <div class="feature-icon">🧠</div>
            <h3>Fun Learning Adventures</h3>
            <p>Turn any topic into an exciting adventure that makes learning fun!</p>
            <a href="/learn" class="feature-button">Start Learning</a>
        </div>
    </div>
    
    <style>
    .feature-showcase {
        display: flex;
        gap: 20px;
        margin: 30px 0;
    }
    
    .feature-card {
        flex: 1;
        background: white;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
    }
    
    .story-card {
        border-top: 5px solid #3b82f6;
    }
    
    .joke-card {
        border-top: 5px solid #f59e0b;
    }
    
    .learn-card {
        border-top: 5px solid #10b981;
    }
    
    .feature-icon {
        font-size: 3em;
        margin-bottom: 15px;
    }
    
    .feature-card h3 {
        margin: 10px 0;
        font-size: 1.5em;
    }
    
    .feature-card p {
        color: #64748b;
        margin-bottom: 20px;
    }
    
    .feature-button {
        display: inline-block;
        padding: 10px 20px;
        background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%);
        color: white;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .feature-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4);
    }
    
    @media (max-width: 768px) {
        .feature-showcase {
            flex-direction: column;
        }
    }
    </style>
    """)
    
    # Quick Start Guide
    with gr.Accordion("🚀 Quick Start Guide", open=True):
        gr.HTML("""
        <div class="quick-start">
            <div class="quick-step">
                <div class="step-number">1</div>
                <div class="step-content">
                    <h4>Choose an Activity</h4>
                    <p>Click on one of the fun activities above - stories, jokes, or learning adventures!</p>
                </div>
            </div>
            
            <div class="quick-step">
                <div class="step-number">2</div>
                <div class="step-content">
                    <h4>Make Your Choices</h4>
                    <p>Follow the simple steps to pick your characters, topics, or joke ingredients.</p>
                </div>
            </div>
            
            <div class="quick-step">
                <div class="step-number">3</div>
                <div class="step-content">
                    <h4>Create & Enjoy!</h4>
                    <p>Press the create button and watch AI turn your choices into something amazing!</p>
                </div>
            </div>
        </div>
        
        <style>
        .quick-start {
            display: flex;
            gap: 15px;
            margin: 20px 0;
        }
        
        .quick-step {
            flex: 1;
            display: flex;
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            border-radius: 12px;
            padding: 15px;
            align-items: center;
        }
        
        .step-number {
            background: #0ea5e9;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            margin-right: 15px;
            flex-shrink: 0;
        }
        
        .step-content h4 {
            margin: 0 0 5px 0;
            color: #0284c7;
        }
        
        .step-content p {
            margin: 0;
            font-size: 0.9em;
            color: #334155;
        }
        
        @media (max-width: 768px) {
            .quick-start {
                flex-direction: column;
            }
        }
        </style>
        """)
    
    # About AI Section with interactive elements
    gr.Markdown("## 🤖 About AI")
    
    with gr.Tabs():
        with gr.TabItem("What is AI?"):
            gr.Markdown("""
            **Artificial Intelligence (AI)** is like having a super smart computer friend that can:
            
            - Create stories and jokes
            - Help you learn new things
            - Answer questions
            - Understand what you're asking for
            
            AI learns by reading lots of books, stories, and information - like a student who's studied millions of books!
            """)
            
        with gr.TabItem("How Does AI Work?"):
            gr.Markdown("""
            1. You give AI your ideas (like picking a hero for your story)
            2. AI uses its "brain" to think about what would make a good story with that hero
            3. It creates something unique just for you
            4. You can keep changing your choices to get different results!
            
            It's like having a helpful friend who knows a lot about stories, jokes, and facts!
            """)
            
        with gr.TabItem("You're in Control!"):
            gr.Markdown("""
            **YOU are the creative director!**
            
            - **You** choose the characters
            - **You** decide the settings
            - **You** pick what to learn about
            - **You** guide the whole adventure
            
            AI just helps bring YOUR ideas to life - like a magical pencil that can draw what you imagine!
            """)
    
    # Fun facts section with interactive visual elements
    gr.Markdown("## 🎯 Fun AI Facts!")
    
    gr.HTML("""
    <div class="fun-facts-container">
        <div class="fun-fact-card">
            <div class="fun-fact-icon">🚀</div>
            <h4>AI can help with:</h4>
            <ul>
                <li>Writing creative stories</li>
                <li>Creating funny jokes</li>
                <li>Explaining complex science</li>
                <li>Making learning fun & exciting</li>
                <li>Answering curious questions</li>
            </ul>
        </div>
        
        <div class="fun-fact-card">
            <div class="fun-fact-icon">🎨</div>
            <h4>You bring the creativity:</h4>
            <ul>
                <li>Choose your own characters</li>
                <li>Pick exciting settings</li>
                <li>Decide what you want to learn</li>
                <li>Guide your adventure</li>
                <li>Make it YOUR unique creation!</li>
            </ul>
        </div>
        
        <div class="fun-fact-card">
            <div class="fun-fact-icon">💡</div>
            <h4>Did you know?</h4>
            <ul>
                <li>AI is like a robot that learned by reading millions of books</li>
                <li>Your choices change what AI creates every time</li>
                <li>Everyone gets different stories and jokes!</li>
                <li>You can create thousands of unique adventures</li>
                <li>AI helps humans be more creative</li>
            </ul>
        </div>
    </div>
    
    <style>
    .fun-facts-container {
        display: flex;
        gap: 20px;
        margin: 20px 0 30px 0;
    }
    
    .fun-fact-card {
        flex: 1;
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border-left: 5px solid #0ea5e9;
    }
    
    .fun-fact-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(14, 165, 233, 0.15);
    }
    
    .fun-fact-card:nth-child(2) {
        border-left-color: #f59e0b;
    }
    
    .fun-fact-card:nth-child(3) {
        border-left-color: #10b981;
    }
    
    .fun-fact-icon {
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    
    .fun-fact-card h4 {
        margin: 0 0 15px 0;
        color: #334155;
    }
    
    .fun-fact-card ul {
        padding-left: 20px;
        margin: 0;
    }
    
    .fun-fact-card li {
        margin-bottom: 8px;
        color: #475569;
    }
    
    @media (max-width: 768px) {
        .fun-facts-container {
            flex-direction: column;
        }
    }
    </style>
    """)
    
    # Parent/Guardian call to action with enhanced visuals
    gr.Markdown("---")
    
    with gr.Row():
        with gr.Column(scale=2):
            gr.HTML("""
            <div class="parent-message">
                <h2>👨‍👩‍👧‍👦 A Message for Parents & Guardians</h2>
                
                <p class="highlight-text">Your child isn't just "using AI"—they're learning to be creative directors of cutting-edge technology.</p>
                
                <p>When children interact with KidsAI, they make every creative decision. They choose the hero, the magical item, the setting. AI simply helps bring <em>their</em> vision to life—like a sophisticated paintbrush responding to an artist's guidance.</p>
                
                <div class="parent-benefit">
                    <div class="benefit-icon">🧠</div>
                    <div class="benefit-text">
                        <h4>Empowerment, Not Replacement</h4>
                        <p>Your child is developing confidence with technology that will be fundamental to their future, while building creative problem-solving skills.</p>
                    </div>
                </div>
                
                <div class="parent-benefit">
                    <div class="benefit-icon">👨‍👩‍👧‍👦</div>
                    <div class="benefit-text">
                        <h4>Best Experienced Together</h4>
                        <p>Children learn better when exploring with trusted adults. You might discover your own creativity sparked by their unique imagination!</p>
                    </div>
                </div>
                
                <div class="parent-benefit">
                    <div class="benefit-icon">🛡️</div>
                    <div class="benefit-text">
                        <h4>Safe & Appropriate</h4>
                        <p>KidsAI is designed specifically for children with appropriate content filters and safety measures in place.</p>
                    </div>
                </div>
            </div>
            
            <style>
            .parent-message {
                background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
                border-radius: 16px;
                padding: 25px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            }
            
            .parent-message h2 {
                margin-top: 0;
                color: #0284c7;
                font-size: 1.8em;
            }
            
            .highlight-text {
                font-size: 1.2em;
                color: #0369a1;
                font-weight: bold;
                padding: 15px;
                background: rgba(255,255,255,0.7);
                border-radius: 8px;
                border-left: 4px solid #0ea5e9;
            }
            
            .parent-benefit {
                display: flex;
                align-items: center;
                margin-top: 20px;
            }
            
            .benefit-icon {
                font-size: 2em;
                margin-right: 15px;
                color: #0ea5e9;
                background: white;
                width: 50px;
                height: 50px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 3px 10px rgba(14, 165, 233, 0.2);
                flex-shrink: 0;
            }
            
            .benefit-text h4 {
                margin: 0 0 5px 0;
                color: #0284c7;
            }
            
            .benefit-text p {
                margin: 0;
                color: #334155;
            }
            </style>
            """)
        
        with gr.Column(scale=1):
            gr.HTML("""
            <div class="parent-cta">
                <h3>🌟 Learn More About Our Mission</h3>
                <p>Discover why KidsAI is designed as a creative partnership tool, plus tips for the best parent-child experience.</p>
                <a href="/parents" class="parent-button">
                    <div class="button-content">
                        <div class="button-icon">👨‍👩‍👧‍👦</div>
                        <div class="button-text">
                            <span>For Parents & Guardians</span>
                            <span class="button-subtext">Tips, safety info & more</span>
                        </div>
                    </div>
                </a>
                
                <div class="privacy-badge">
                    <div class="badge-icon">🛡️</div>
                    <div class="badge-text">Kid-Safe & Privacy Focused</div>
                </div>
            </div>
            
            <style>
            .parent-cta {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 25px;
                border-radius: 16px;
                color: white;
                box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
                height: 100%;
                display: flex;
                flex-direction: column;
            }
            
            .parent-cta h3 {
                margin-top: 0;
                font-size: 1.5em;
            }
            
            .parent-cta p {
                margin-bottom: 20px;
            }
            
            .parent-button {
                display: block;
                background: white;
                color: #667eea;
                padding: 15px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: bold;
                transition: all 0.3s ease;
                margin-top: auto;
            }
            
            .parent-button:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
            }
            
            .button-content {
                display: flex;
                align-items: center;
            }
            
            .button-icon {
                font-size: 1.5em;
                margin-right: 15px;
            }
            
            .button-text {
                display: flex;
                flex-direction: column;
            }
            
            .button-subtext {
                font-size: 0.8em;
                font-weight: normal;
                opacity: 0.8;
            }
            
            .privacy-badge {
                display: flex;
                align-items: center;
                background: rgba(255,255,255,0.2);
                border-radius: 25px;
                padding: 10px 15px;
                margin-top: 20px;
            }
            
            .badge-icon {
                margin-right: 10px;
            }
            
            .badge-text {
                font-size: 0.9em;
                font-weight: bold;
            }
            </style>
            """)
    
    # Getting started - Enhanced version
    gr.Markdown("---")
    
    # Animated call to action
    gr.HTML("""
    <div class="start-adventure">
        <div class="adventure-content">
            <h2>🚀 Ready to start your adventure?</h2>
            <p>Choose any activity from the colorful buttons above to begin!</p>
            <p>Each adventure is designed to be fun, educational, and spark your creativity!</p>
        </div>
        <div class="adventure-animation">
            <div class="floating-icon" style="animation-delay: 0s;">🚀</div>
            <div class="floating-icon" style="animation-delay: 1s;">✨</div>
            <div class="floating-icon" style="animation-delay: 2s;">🦄</div>
            <div class="floating-icon" style="animation-delay: 3s;">🌟</div>
            <div class="floating-icon" style="animation-delay: 4s;">🧠</div>
        </div>
    </div>
    
    <style>
    .start-adventure {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        border-radius: 16px;
        padding: 30px;
        color: white;
        text-align: center;
        position: relative;
        overflow: hidden;
        margin: 30px 0;
    }
    
    .adventure-content {
        position: relative;
        z-index: 2;
    }
    
    .adventure-content h2 {
        margin-top: 0;
        font-size: 2em;
    }
    
    .adventure-animation {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
    }
    
    .floating-icon {
        position: absolute;
        font-size: 2em;
        opacity: 0.3;
        animation: float 8s infinite ease-in-out;
    }
    
    .floating-icon:nth-child(1) { top: 20%; left: 10%; }
    .floating-icon:nth-child(2) { top: 10%; left: 30%; }
    .floating-icon:nth-child(3) { top: 30%; left: 70%; }
    .floating-icon:nth-child(4) { top: 60%; left: 20%; }
    .floating-icon:nth-child(5) { top: 50%; left: 85%; }
    
    @keyframes float {
        0% { transform: translateY(0) rotate(0); }
        50% { transform: translateY(-20px) rotate(10deg); }
        100% { transform: translateY(0) rotate(0); }
    }
    </style>
    """)
    
    # Enhanced Tips section
    with gr.Accordion("💡 Tips for the best experience", open=False):
        gr.HTML("""
        <div class="tips-container">
            <div class="tip-card">
                <div class="tip-icon">⏱️</div>
                <div class="tip-content">
                    <h4>Take your time</h4>
                    <p>There's no rush! Explore and have fun at your own pace.</p>
                </div>
            </div>
            
            <div class="tip-card">
                <div class="tip-icon">🔄</div>
                <div class="tip-content">
                    <h4>Try different combinations</h4>
                    <p>Each choice creates a unique experience. Mix and match!</p>
                </div>
            </div>
            
            <div class="tip-card">
                <div class="tip-icon">🗣️</div>
                <div class="tip-content">
                    <h4>Read creations out loud</h4>
                    <p>Stories and jokes are even better when read aloud together!</p>
                </div>
            </div>
            
            <div class="tip-card">
                <div class="tip-icon">❓</div>
                <div class="tip-content">
                    <h4>Ask questions</h4>
                    <p>If you're curious about how something works, explore and discover!</p>
                </div>
            </div>
            
            <div class="tip-card">
                <div class="tip-icon">🎨</div>
                <div class="tip-content">
                    <h4>Be creative</h4>
                    <p>Your imagination is the most important ingredient!</p>
                </div>
            </div>
        </div>
        
        <style>
        .tips-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }
        
        .tip-card {
            display: flex;
            align-items: center;
            background: white;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
        }
        
        .tip-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .tip-icon {
            font-size: 2em;
            margin-right: 15px;
            color: #0ea5e9;
            flex-shrink: 0;
        }
        
        .tip-content h4 {
            margin: 0 0 5px 0;
            color: #334155;
        }
        
        .tip-content p {
            margin: 0;
            color: #64748b;
        }
        
        @media (max-width: 768px) {
            .tips-container {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """)

    # Session Recovery Feature
    with gr.Accordion("💾 Your Previous Creations", open=False):
        gr.HTML("""
        <div class="session-notice">
            <div class="notice-icon">�</div>
            <div class="notice-text">
                <h4>Privacy First</h4>
                <p>Your creations stay private! We don't save anything you make - it's just for you to enjoy right now.</p>
                <p>This keeps your imagination safe and secure! 🛡️</p>
            </div>
        </div>
        
        <style>
        .session-notice {
            display: flex;
            align-items: center;
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            border-radius: 12px;
            padding: 20px;
            margin-top: 15px;
        }
        
        .notice-icon {
            font-size: 2.5em;
            margin-right: 20px;
            color: #0ea5e9;
        }
        
        .notice-text h4 {
            margin: 0 0 10px 0;
            color: #0284c7;
        }
        
        .notice-text p {
            margin: 0 0 5px 0;
            color: #334155;
        }
        </style>
        """)

if __name__ == "__main__":
    demo.launch()
