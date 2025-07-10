# pages/parents_page.py
import gradio as gr

with gr.Blocks() as demo:
    # Hero section with enhanced visuals
    gr.HTML("""
    <div class="parents-hero">
        <div class="hero-content">
            <h1>👨‍👩‍👧‍👦 For Parents & Guardians</h1>
            <p class="hero-subtitle">Understanding the Mission Behind KidsAI</p>
        </div>
    </div>
    
    <style>
    .parents-hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
        margin-bottom: 30px;
    }
    
    .hero-content h1 {
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        font-size: 1.3em;
        opacity: 0.9;
        margin: 0;
    }
    </style>
    """)
    
    # Mission statement with enhanced visual design
    gr.HTML("""
    <div class="mission-section">
        <div class="mission-card">
            <div class="mission-icon">🎯</div>
            <div class="mission-content">
                <h2>Why I Built KidsAI</h2>
                <p class="mission-intro">As we stand at the threshold of an AI-driven future, I believe we have a choice: we can either prepare our children to understand and harness this technology responsibly, or we can leave them to discover it without guidance.</p>
                
                <div class="key-message">
                    <strong>KidsAI isn't about replacing creativity—it's about amplifying it.</strong>
                </div>
                
                <p>When your child uses KidsAI, they aren't becoming passive consumers of AI-generated content. They are becoming <strong>creative directors</strong>, making choices, guiding narratives, and learning that technology is a tool that responds to <em>their</em> imagination.</p>
            </div>
        </div>
    </div>
    
    <style>
    .mission-section {
        margin-bottom: 30px;
    }
    
    .mission-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 16px;
        padding: 30px;
        display: flex;
        align-items: flex-start;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-left: 5px solid #0ea5e9;
    }
    
    .mission-icon {
        font-size: 3em;
        margin-right: 25px;
        color: #0ea5e9;
        background: white;
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 5px 15px rgba(14, 165, 233, 0.2);
        flex-shrink: 0;
    }
    
    .mission-content h2 {
        margin-top: 0;
        color: #0284c7;
        font-size: 2em;
    }
    
    .mission-intro {
        font-size: 1.1em;
        color: #334155;
        line-height: 1.6;
    }
    
    .key-message {
        background: rgba(14, 165, 233, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
        border-left: 4px solid #0ea5e9;
        font-size: 1.2em;
        color: #0369a1;
    }
    
    @media (max-width: 768px) {
        .mission-card {
            flex-direction: column;
            text-align: center;
        }
        
        .mission-icon {
            margin-right: 0;
            margin-bottom: 20px;
        }
    }
    </style>
    """)
    
    # Core philosophy section with enhanced visual cards
    gr.HTML("""
    <div class="philosophy-section">
        <h2 class="section-title">🧭 The Philosophy: Creative Partnership, Not Replacement</h2>
        
        <div class="philosophy-cards">
            <div class="philosophy-card artist-card">
                <div class="card-icon">🎨</div>
                <div class="card-content">
                    <h3>Your Child is the Artist</h3>
                    <p>Think of AI like a sophisticated paintbrush. The brush doesn't create the painting—the artist does. Similarly, when your child selects a "Brave Knight," "Magic Boots," and "Enchanted Forest," <strong>they</strong> are crafting the creative vision. AI simply helps bring that vision to life.</p>
                    <div class="highlight-box">
                        <strong>The creativity is 100% theirs.</strong>
                    </div>
                </div>
            </div>
            
            <div class="philosophy-card safety-card">
                <div class="card-icon">🛡️</div>
                <div class="card-content">
                    <h3>Safety by Design</h3>
                    <p>KidsAI uses a "promptless" interface—no free text input—making harmful content impossible by design. Every output goes through a dedicated safety review system before reaching your child.</p>
                    <div class="highlight-box">
                        <strong>Trust through engineering, not just promises.</strong>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <style>
    .philosophy-section {
        margin: 40px 0;
    }
    
    .section-title {
        text-align: center;
        color: #334155;
        font-size: 2em;
        margin-bottom: 30px;
    }
    
    .philosophy-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 25px;
        margin-top: 20px;
    }
    
    .philosophy-card {
        background: white;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .philosophy-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .artist-card {
        border-top: 5px solid #f59e0b;
    }
    
    .safety-card {
        border-top: 5px solid #10b981;
    }
    
    .card-icon {
        font-size: 3em;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .card-content h3 {
        color: #334155;
        margin-bottom: 15px;
        font-size: 1.5em;
        text-align: center;
    }
    
    .card-content p {
        color: #64748b;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        color: #0369a1;
        font-size: 1.1em;
        border-left: 4px solid #0ea5e9;
    }
    
    @media (max-width: 768px) {
        .philosophy-cards {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """)
    
    # The "why now" section with enhanced visuals
    gr.HTML("""
    <div class="why-now-section">
        <h2 class="section-title">🌍 Why This Matters Now</h2>
        
        <div class="future-reality-card">
            <div class="reality-icon">🚀</div>
            <div class="reality-content">
                <h3>The Reality of Our Children's Future</h3>
                <p>AI will be as fundamental to your child's world as the internet is today. Just as we taught digital literacy, we now need to foster <strong>AI literacy</strong>—but safely, positively, and early.</p>
                <div class="goal-highlight">
                    The goal isn't to create AI experts; it's to create confident, creative thinkers who see technology as a tool for expression, not a mysterious black box.
                </div>
            </div>
        </div>
        
        <div class="magic-cards">
            <div class="magic-card moment-card">
                <div class="card-header">
                    <div class="card-emoji">🎭</div>
                    <h3>The Magic Moment</h3>
                </div>
                <p>When a 6-year-old presses a few buttons and generates a unique story that never existed before—a story that is truly <em>theirs</em>—they experience a powerful "I made this!" moment.</p>
                <div class="card-emphasis">
                    This isn't about consuming technology; it's about <strong>commanding it to serve their imagination</strong>.
                </div>
            </div>
            
            <div class="magic-card confidence-card">
                <div class="card-header">
                    <div class="card-emoji">🌱</div>
                    <h3>Building Creative Confidence</h3>
                </div>
                <p>In a world where AI can generate content instantly, the most valuable skill isn't technical proficiency—it's <strong>creative vision</strong>. KidsAI nurtures this by putting your child in the director's chair.</p>
                <div class="card-emphasis">
                    Your child learns to be the creative director, making all the important decisions.
                </div>
            </div>
        </div>
    </div>
    
    <style>
    .why-now-section {
        margin: 40px 0;
    }
    
    .future-reality-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 30px;
        display: flex;
        align-items: flex-start;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-left: 5px solid #0ea5e9;
    }
    
    .reality-icon {
        font-size: 3em;
        margin-right: 25px;
        color: #0ea5e9;
        background: white;
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 5px 15px rgba(14, 165, 233, 0.2);
        flex-shrink: 0;
    }
    
    .reality-content h3 {
        margin-top: 0;
        color: #0284c7;
        font-size: 1.8em;
    }
    
    .goal-highlight {
        background: rgba(14, 165, 233, 0.1);
        border-radius: 8px;
        padding: 15px;
        margin-top: 15px;
        border-left: 4px solid #0ea5e9;
        font-style: italic;
        color: #0369a1;
    }
    
    .magic-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 25px;
    }
    
    .magic-card {
        background: white;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .magic-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .moment-card {
        border-top: 5px solid #8b5cf6;
    }
    
    .confidence-card {
        border-top: 5px solid #10b981;
    }
    
    .card-header {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    
    .card-emoji {
        font-size: 2em;
        margin-right: 15px;
    }
    
    .card-header h3 {
        margin: 0;
        color: #334155;
        font-size: 1.3em;
    }
    
    .card-emphasis {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 8px;
        padding: 12px;
        margin-top: 15px;
        font-weight: bold;
        color: #475569;
        border-left: 4px solid #64748b;
    }
    
    @media (max-width: 768px) {
        .future-reality-card {
            flex-direction: column;
            text-align: center;
        }
        
        .reality-icon {
            margin-right: 0;
            margin-bottom: 20px;
        }
        
        .magic-cards {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """)
    
    # Addressing concerns with enhanced accordion styling
    gr.HTML("""
    <div class="concerns-section">
        <h2 class="section-title">🤔 Addressing Common Concerns</h2>
        <div class="concerns-intro">
            <p>We understand that introducing AI to children raises important questions. Here are thoughtful responses to the most common concerns:</p>
        </div>
    </div>
    
    <style>
    .concerns-section {
        margin: 40px 0 20px 0;
    }
    
    .concerns-intro {
        background: linear-gradient(135deg, #fef3c7 0%, #fef08a 100%);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #f59e0b;
    }
    
    .concerns-intro p {
        margin: 0;
        color: #92400e;
        font-size: 1.1em;
    }
    </style>
    """)
    
    with gr.Accordion("\"Won't this make my child dependent on AI for creativity?\"", open=False):
        gr.HTML("""
        <div class="concern-answer">
            <div class="answer-icon">🎨</div>
            <div class="answer-content">
                <p><strong>Quite the opposite.</strong> KidsAI teaches children that AI is a <em>tool that responds to their choices</em>. They learn to be the creative director, making decisions about characters, settings, and outcomes. This builds creative confidence and decision-making skills.</p>
                
                <div class="comparison-box">
                    <div class="comparison-item bad">
                        <span class="comparison-label">❌ Passive consumption:</span>
                        <span>Watching pre-made content</span>
                    </div>
                    <div class="comparison-item good">
                        <span class="comparison-label">✅ Active creation:</span>
                        <span>Your child shapes the narrative</span>
                    </div>
                </div>
            </div>
        </div>
        
        <style>
        .concern-answer {
            display: flex;
            align-items: flex-start;
            margin-top: 15px;
        }
        
        .answer-icon {
            font-size: 2.5em;
            margin-right: 20px;
            flex-shrink: 0;
        }
        
        .answer-content {
            flex: 1;
        }
        
        .comparison-box {
            margin-top: 15px;
            background: #f8fafc;
            border-radius: 8px;
            padding: 15px;
        }
        
        .comparison-item {
            display: flex;
            align-items: center;
            margin-bottom: 8px;
        }
        
        .comparison-item:last-child {
            margin-bottom: 0;
        }
        
        .comparison-label {
            font-weight: bold;
            margin-right: 10px;
            min-width: 140px;
        }
        
        .comparison-item.good .comparison-label {
            color: #059669;
        }
        
        .comparison-item.bad .comparison-label {
            color: #dc2626;
        }
        </style>
        """)
    
    with gr.Accordion("\"Is my child too young to understand AI?\"", open=False):
        gr.HTML("""
        <div class="concern-answer">
            <div class="answer-icon">🧠</div>
            <div class="answer-content">
                <p>Children are natural learners and surprisingly adaptable to new technologies. KidsAI introduces AI concepts through play and creation, not complex technical explanations.</p>
                
                <div class="analogy-box">
                    <p><strong>They don't need to understand the mechanics of AI any more than they need to understand combustion engines to benefit from cars.</strong> They need to understand that it's a tool that responds to their creativity.</p>
                </div>
                
                <div class="age-benefits">
                    <h4>Age-Appropriate Learning:</h4>
                    <ul>
                        <li><strong>Ages 3-5:</strong> "I press buttons and magic stories appear!"</li>
                        <li><strong>Ages 6-8:</strong> "My choices change what the computer creates!"</li>
                        <li><strong>Ages 9-10:</strong> "I'm teaching the AI what kind of story I want!"</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <style>
        .analogy-box {
            background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
            border-left: 4px solid #0ea5e9;
            font-style: italic;
        }
        
        .age-benefits {
            background: #f0f9ff;
            border-radius: 8px;
            padding: 15px;
            margin-top: 15px;
        }
        
        .age-benefits h4 {
            margin-top: 0;
            color: #0284c7;
        }
        
        .age-benefits ul {
            margin-bottom: 0;
        }
        
        .age-benefits li {
            margin-bottom: 8px;
        }
        </style>
        """)
    
    with gr.Accordion("\"What about screen time and digital wellness?\"", open=False):
        gr.HTML("""
        <div class="concern-answer">
            <div class="answer-icon">⏰</div>
            <div class="answer-content">
                <p>KidsAI is designed for <strong>quality over quantity</strong>. Sessions are naturally brief (5-10 minutes) and focused on creative output rather than endless scrolling.</p>
                
                <div class="wellness-points">
                    <div class="wellness-point">
                        <div class="point-icon">🎯</div>
                        <div class="point-text">
                            <strong>Goal-oriented sessions:</strong> Create something, enjoy it, share it, then move on
                        </div>
                    </div>
                    
                    <div class="wellness-point">
                        <div class="point-icon">🚫</div>
                        <div class="point-text">
                            <strong>No infinite scroll:</strong> Natural stopping points prevent endless use
                        </div>
                    </div>
                    
                    <div class="wellness-point">
                        <div class="point-icon">✨</div>
                        <div class="point-text">
                            <strong>Inspiration, not addiction:</strong> Designed to spark offline creativity
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <style>
        .wellness-points {
            margin-top: 15px;
        }
        
        .wellness-point {
            display: flex;
            align-items: center;
            background: white;
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .point-icon {
            font-size: 1.5em;
            margin-right: 15px;
            flex-shrink: 0;
        }
        
        .point-text {
            flex: 1;
        }
        </style>
        """)
    
    # The bigger picture with enhanced design
    gr.HTML("""
    <div class="bigger-picture-section">
        <h2 class="section-title">🚀 The Bigger Picture: Foundation for Life</h2>
        
        <div class="foundation-card">
            <div class="foundation-header">
                <div class="foundation-icon">🌟</div>
                <h3>Building Tomorrow's Thinkers</h3>
            </div>
            <p>KidsAI is my proof-of-concept for a larger mission: building AI that is truly worthy of a child's trust. The safety architecture, creative partnership model, and educational approach demonstrated here lay the groundwork for more sophisticated AI companions as children grow.</p>
            <div class="mission-statement">
                This isn't just about stories and jokes—it's about establishing a healthy, empowering relationship with AI technology from day one.
            </div>
        </div>
        
        <div class="learning-benefits">
            <div class="benefit-column learns-column">
                <div class="column-header">
                    <div class="column-icon">🌟</div>
                    <h3>What Your Child Learns</h3>
                </div>
                <ul class="benefit-list">
                    <li><span class="benefit-icon">🎯</span><strong>Decision-making:</strong> Every choice shapes the outcome</li>
                    <li><span class="benefit-icon">🎨</span><strong>Creative ownership:</strong> Their ideas drive the experience</li>
                    <li><span class="benefit-icon">💻</span><strong>Technology confidence:</strong> AI responds to their commands</li>
                    <li><span class="benefit-icon">🧠</span><strong>Critical thinking:</strong> Understanding cause and effect</li>
                    <li><span class="benefit-icon">💬</span><strong>Communication:</strong> Expressing ideas through selections</li>
                </ul>
            </div>
            
            <div class="benefit-column benefits-column">
                <div class="column-header">
                    <div class="column-icon">🎯</div>
                    <h3>Long-term Benefits</h3>
                </div>
                <ul class="benefit-list">
                    <li><span class="benefit-icon">🚀</span>Confident interaction with future AI tools</li>
                    <li><span class="benefit-icon">🤝</span>Understanding of human-AI collaboration</li>
                    <li><span class="benefit-icon">⚡</span>Strong creative problem-solving skills</li>
                    <li><span class="benefit-icon">💚</span>Healthy relationship with technology</li>
                    <li><span class="benefit-icon">🔓</span>Reduced fear or mystification of AI</li>
                </ul>
            </div>
        </div>
    </div>
    
    <style>
    .bigger-picture-section {
        margin: 40px 0;
    }
    
    .foundation-card {
        background: linear-gradient(135deg, #fef3c7 0%, #fed7aa 100%);
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 30px;
        box-shadow: 0 5px 15px rgba(245, 158, 11, 0.2);
        border-left: 5px solid #f59e0b;
    }
    
    .foundation-header {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    
    .foundation-icon {
        font-size: 3em;
        margin-right: 20px;
        color: #d97706;
    }
    
    .foundation-header h3 {
        margin: 0;
        color: #92400e;
        font-size: 2em;
    }
    
    .foundation-card p {
        color: #78350f;
        font-size: 1.1em;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    
    .mission-statement {
        background: rgba(217, 119, 6, 0.2);
        border-radius: 8px;
        padding: 15px;
        border-left: 4px solid #d97706;
        font-weight: bold;
        color: #92400e;
        font-style: italic;
    }
    
    .learning-benefits {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 25px;
    }
    
    .benefit-column {
        background: white;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .benefit-column:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .learns-column {
        border-top: 5px solid #3b82f6;
    }
    
    .benefits-column {
        border-top: 5px solid #10b981;
    }
    
    .column-header {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    
    .column-icon {
        font-size: 2.5em;
        margin-right: 15px;
    }
    
    .column-header h3 {
        margin: 0;
        color: #334155;
        font-size: 1.5em;
    }
    
    .benefit-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .benefit-list li {
        display: flex;
        align-items: center;
        margin-bottom: 12px;
        padding: 8px 0;
    }
    
    .benefit-icon {
        font-size: 1.2em;
        margin-right: 12px;
        width: 20px;
        flex-shrink: 0;
    }
    
    @media (max-width: 768px) {
        .foundation-header {
            flex-direction: column;
            text-align: center;
        }
        
        .foundation-icon {
            margin-right: 0;
            margin-bottom: 15px;
        }
        
        .learning-benefits {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """)
    
    # Important disclaimer with enhanced styling
    gr.HTML("""
    <div class="guidance-warning">
        <div class="warning-content">
            <div class="warning-icon">⚠️</div>
            <div class="warning-text">
                <h3>Important: We Highly Recommend Parental Guidance</h3>
                <p><strong>KidsAI is designed to be explored together.</strong> Children are naturally more engaged and learn better when sharing experiences with trusted adults. Your presence transforms a digital activity into a bonding moment and learning opportunity.</p>
            </div>
        </div>
    </div>
    
    <style>
    .guidance-warning {
        margin: 40px 0;
    }
    
    .warning-content {
        background: linear-gradient(135deg, #fef3c7 0%, #fcd34d 100%);
        border-left: 6px solid #f59e0b;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.2);
        display: flex;
        align-items: center;
    }
    
    .warning-icon {
        font-size: 3em;
        margin-right: 20px;
        color: #d97706;
        flex-shrink: 0;
    }
    
    .warning-text h3 {
        margin: 0 0 10px 0;
        color: #92400e;
        font-size: 1.5em;
    }
    
    .warning-text p {
        margin: 0;
        color: #92400e;
        font-size: 1.1em;
        line-height: 1.6;
    }
    
    @media (max-width: 768px) {
        .warning-content {
            flex-direction: column;
            text-align: center;
        }
        
        .warning-icon {
            margin-right: 0;
            margin-bottom: 15px;
        }
    }
    </style>
    """)
    
    # Call to action with enhanced design
    gr.HTML("""
    <div class="cta-section">
        <h2 class="section-title">💫 Ready to Explore Together?</h2>
        
        <div class="experience-cards">
            <div class="experience-card parent-child-card">
                <div class="card-header">
                    <div class="card-icon">🎯</div>
                    <h3>The Parent-Child Experience</h3>
                </div>
                <p><strong>Sit with your child during their KidsAI sessions.</strong> Your engagement amplifies their excitement and learning:</p>
                
                <div class="tip-list">
                    <div class="tip-item">
                        <span class="tip-icon">💭</span>
                        <span><strong>Ask about their choices:</strong> "Why did you pick the brave knight? What do you think will happen?"</span>
                    </div>
                    <div class="tip-item">
                        <span class="tip-icon">🎉</span>
                        <span><strong>Celebrate their creativity:</strong> "Wow! YOU created this amazing story!"</span>
                    </div>
                    <div class="tip-item">
                        <span class="tip-icon">🔗</span>
                        <span><strong>Make connections:</strong> "This reminds me of that book we read together..."</span>
                    </div>
                    <div class="tip-item">
                        <span class="tip-icon">✨</span>
                        <span><strong>Share the wonder:</strong> You might be surprised by the creative combinations they discover!</span>
                    </div>
                </div>
            </div>
            
            <div class="experience-card creation-card">
                <div class="card-header">
                    <div class="card-icon">👨‍👩‍👧‍👦</div>
                    <h3>You Might Create Something Amazing Too!</h3>
                </div>
                <p>Don't be surprised if you find yourself just as fascinated by the creative possibilities. Many parents discover that:</p>
                
                <div class="discovery-list">
                    <div class="discovery-item">
                        <span class="discovery-icon">🤝</span>
                        <span><strong>You become co-creators</strong> in the storytelling process</span>
                    </div>
                    <div class="discovery-item">
                        <span class="discovery-icon">💡</span>
                        <span><strong>Your own creativity is sparked</strong> by your child's unique choices</span>
                    </div>
                    <div class="discovery-item">
                        <span class="discovery-icon">🧠</span>
                        <span><strong>You gain insights</strong> into how your child thinks and imagines</span>
                    </div>
                    <div class="discovery-item">
                        <span class="discovery-icon">💝</span>
                        <span><strong>You create shared memories</strong> around these collaborative stories</span>
                    </div>
                </div>
                
                <div class="special-note">
                    This isn't just screen time—it's creative time together.
                </div>
            </div>
        </div>
    </div>
    
    <style>
    .cta-section {
        margin: 40px 0;
    }
    
    .experience-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 25px;
        margin-top: 20px;
    }
    
    .experience-card {
        background: white;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .experience-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .parent-child-card {
        border-top: 5px solid #3b82f6;
    }
    
    .creation-card {
        border-top: 5px solid #8b5cf6;
    }
    
    .card-header {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    
    .card-icon {
        font-size: 2.5em;
        margin-right: 15px;
    }
    
    .card-header h3 {
        margin: 0;
        color: #334155;
        font-size: 1.3em;
    }
    
    .tip-list, .discovery-list {
        margin-top: 15px;
    }
    
    .tip-item, .discovery-item {
        display: flex;
        align-items: flex-start;
        margin-bottom: 12px;
        padding: 8px 0;
    }
    
    .tip-icon, .discovery-icon {
        font-size: 1.2em;
        margin-right: 12px;
        margin-top: 2px;
        flex-shrink: 0;
    }
    
    .special-note {
        background: linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%);
        border-radius: 8px;
        padding: 15px;
        margin-top: 20px;
        text-align: center;
        font-weight: bold;
        color: #7c3aed;
        border-left: 4px solid #8b5cf6;
    }
    
    @media (max-width: 768px) {
        .experience-cards {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """)
    
    # Getting started guide with enhanced visuals
    gr.HTML("""
    <div class="getting-started-section">
        <h2 class="section-title">🌟 Making It Easy to Get Started</h2>
        
        <div class="getting-started-card">
            <h3>First Session Tips:</h3>
            
            <div class="tips-grid">
                <div class="tip-card">
                    <div class="tip-number">1</div>
                    <div class="tip-content">
                        <h4>Start together</h4>
                        <p>Explore the interface with your child in the first session</p>
                    </div>
                </div>
                
                <div class="tip-card">
                    <div class="tip-number">2</div>
                    <div class="tip-content">
                        <h4>Let them lead</h4>
                        <p>Allow your child to make the creative choices while you provide encouragement</p>
                    </div>
                </div>
                
                <div class="tip-card">
                    <div class="tip-number">3</div>
                    <div class="tip-content">
                        <h4>Read aloud</h4>
                        <p>Take turns reading the generated stories together</p>
                    </div>
                </div>
                
                <div class="tip-card">
                    <div class="tip-number">4</div>
                    <div class="tip-content">
                        <h4>Ask open questions</h4>
                        <p>"What would you change?" "What happens next?"</p>
                    </div>
                </div>
                
                <div class="tip-card">
                    <div class="tip-number">5</div>
                    <div class="tip-content">
                        <h4>Save or share</h4>
                        <p>Consider printing favorite stories or sharing them with family</p>
                    </div>
                </div>
            </div>
            
            <div class="final-message">
                <strong>This is their tool, their creativity, their future—guided by your wisdom and enhanced by your presence.</strong>
            </div>
        </div>
    </div>
    
    <style>
    .getting-started-section {
        margin: 40px 0;
    }
    
    .getting-started-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-left: 5px solid #0ea5e9;
    }
    
    .getting-started-card h3 {
        margin-top: 0;
        color: #0284c7;
        font-size: 1.8em;
        text-align: center;
        margin-bottom: 25px;
    }
    
    .tips-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 15px;
        margin-bottom: 25px;
    }
    
    .tip-card {
        background: white;
        border-radius: 12px;
        padding: 15px;
        display: flex;
        align-items: center;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .tip-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(14, 165, 233, 0.2);
    }
    
    .tip-number {
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
    
    .tip-content h4 {
        margin: 0 0 5px 0;
        color: #334155;
        font-size: 1em;
    }
    
    .tip-content p {
        margin: 0;
        color: #64748b;
        font-size: 0.9em;
    }
    
    .final-message {
        background: rgba(14, 165, 233, 0.1);
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        color: #0369a1;
        font-size: 1.1em;
        border-left: 4px solid #0ea5e9;
    }
    
    @media (max-width: 768px) {
        .tips-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
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
