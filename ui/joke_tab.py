# ui/joke_tab.py
import gradio as gr
from logic.llm_interface import JOKE_SUBJECTS_1, JOKE_SUBJECTS_2, safe_generate_joke

def create_joke_tab():
    """Creates the UI for the Joke Factory tab with guided step-by-step interface."""
    
    # State variables to track selections and current step
    selected_subject1 = gr.State("")
    selected_subject2 = gr.State("")
    current_step = gr.State(1)  # 1=first subject, 2=second subject, 3=ready
    
    # First subject selection (initially visible)
    subject1_section = gr.Column(visible=True)
    with subject1_section:
        gr.Markdown("**What should we start our joke with?**")
        with gr.Row():
            subject1_buttons = []
            for subject in JOKE_SUBJECTS_1:
                btn = gr.Button(subject, variant="secondary", size="lg")
                subject1_buttons.append(btn)
    
    # Second subject selection (initially hidden)
    subject2_section = gr.Column(visible=False)
    with subject2_section:
        gr.Markdown("**What should we mix it with?**")
        with gr.Row():
            subject2_buttons = []
            for subject in JOKE_SUBJECTS_2:
                btn = gr.Button(subject, variant="secondary", size="lg")
                subject2_buttons.append(btn)
    
    # Summary and create button (initially hidden)
    summary_section = gr.Column(visible=False)
    with summary_section:
        gr.Markdown("**🎉 Perfect! Let's see what funny thing happens when we mix:**")
        selection_summary = gr.Markdown("")
        create_btn = gr.Button("🤣 Tell Me The Joke!", variant="primary", size="lg")
    
    # Loading animation (initially hidden)
    loading_html = gr.HTML(visible=False, value="""
        <div style="text-align: center; padding: 20px;">
            <div style="display: inline-block; animation: bounce 1s infinite; font-size: 3em;">😂</div>
            <div style="margin-top: 10px; font-style: italic; color: #666;">Cooking up something hilarious...</div>
        </div>
        <style>
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-15px); }
                60% { transform: translateY(-10px); }
            }
        </style>
    """)
    
    # Joke output (initially hidden)
    joke_output = gr.Textbox(label="🎭 Your Hilarious Joke", interactive=False, lines=4, visible=False)
    
    # AI celebration section (initially hidden)
    ai_celebration = gr.Column(visible=False)
    with ai_celebration:
        gr.Markdown("### 🤖🎉 You just created this joke with Artificial Intelligence!")
        gr.Markdown("You picked the ingredients, and AI mixed them into something funny! 😄")
        gr.Markdown("**Did you know?** Computers can learn to be funny by reading lots of jokes!")
    
    new_joke_btn = gr.Button("🎪 Make Another Joke!", variant="secondary", visible=False)
    
    # Helper functions for guided experience
    def select_subject1(subject_choice):
        """Handle first subject selection and move to next step"""
        return (
            subject_choice,  # selected_subject1
            2,  # current_step (move to second subject)
            gr.Column(visible=False),  # subject1_section
            gr.Column(visible=True),   # subject2_section
            gr.Column(visible=False)   # summary_section
        )
    
    def select_subject2(subject_choice, subject1):
        """Handle second subject selection and show summary"""
        summary_text = f"""
**🎯 First Thing:** {subject1}  
**🎲 Second Thing:** {subject_choice}  

**What happens when we mix them? Let's find out!** 🤔➡️😂
        """
        return (
            subject_choice,  # selected_subject2
            3,  # current_step (ready to create)
            gr.Column(visible=False),  # subject1_section
            gr.Column(visible=False),  # subject2_section
            gr.Column(visible=True),   # summary_section
            summary_text  # selection_summary
        )
    
    def generate_joke(subject1, subject2):
        """Generate the joke and show loading/result"""
        # Hide summary section and show loading
        yield (
            gr.Column(visible=False),    # summary_section
            gr.HTML(visible=True),       # loading
            gr.Textbox(visible=False),   # joke
            gr.Column(visible=False),    # ai_celebration
            gr.Button(visible=False)     # new joke button
        )
        
        # Generate joke
        joke_text = safe_generate_joke(subject1, subject2)
        
        # Show result with AI celebration
        yield (
            gr.Column(visible=False),    # summary_section (keep hidden)
            gr.HTML(visible=False),      # loading
            gr.Textbox(value=joke_text, visible=True),  # joke
            gr.Column(visible=True),     # ai_celebration
            gr.Button(visible=True)      # new joke button
        )
    
    def reset_joke():
        """Reset everything back to step 1"""
        return (
            "",  # selected_subject1
            "",  # selected_subject2
            1,   # current_step
            gr.Column(visible=True),   # subject1_section
            gr.Column(visible=False),  # subject2_section
            gr.Column(visible=False),  # summary_section
            "",  # selection_summary
            gr.Textbox(visible=False, value=""),  # joke_output
            gr.Column(visible=False),  # ai_celebration
            gr.Button(visible=False)   # new_joke_btn
        )
    
    # Connect first subject buttons
    for i, btn in enumerate(subject1_buttons):
        btn.click(
            fn=lambda i=i: select_subject1(JOKE_SUBJECTS_1[i]),
            outputs=[selected_subject1, current_step, 
                    subject1_section, subject2_section, summary_section]
        )
    
    # Connect second subject buttons
    for i, btn in enumerate(subject2_buttons):
        btn.click(
            fn=lambda subject1, i=i: select_subject2(JOKE_SUBJECTS_2[i], subject1),
            inputs=[selected_subject1],
            outputs=[selected_subject2, current_step,
                    subject1_section, subject2_section, summary_section, selection_summary]
        )
    
    # Connect create joke button
    create_btn.click(
        fn=generate_joke,
        inputs=[selected_subject1, selected_subject2],
        outputs=[summary_section, loading_html, joke_output, ai_celebration, new_joke_btn]
    )
    
    # Connect new joke button
    new_joke_btn.click(
        fn=reset_joke,
        outputs=[selected_subject1, selected_subject2, current_step,
                subject1_section, subject2_section, summary_section, 
                selection_summary, joke_output, ai_celebration, new_joke_btn]
    )
    
    # Return empty for compatibility with existing interface
    # The old interface expected btn, inputs, outputs but the new guided interface handles everything internally
    return gr.Button(visible=False), [], []