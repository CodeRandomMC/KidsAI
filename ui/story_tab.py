# ui/story_tab.py
import gradio as gr
from logic.llm_interface import STORY_HEROES, STORY_ITEMS, STORY_SETTINGS, safe_generate_story

# Character icons for visual recognition
HERO_ICONS = {
    "Princess": "👸",
    "Knight": "🛡️",
    "Dragon": "🐉",
    "Wizard": "🧙‍♂️", 
    "Pirate": "🏴‍☠️",
    "Robot": "🤖",
    "Unicorn": "🦄",
    "Superhero": "🦸‍♀️"
}

ITEM_ICONS = {
    "Magic Wand": "🪄",
    "Sword": "⚔️",
    "Shield": "🛡️",
    "Crown": "👑",
    "Map": "🗺️",
    "Key": "🔑",
    "Book": "📚",
    "Crystal": "💎"
}

SETTING_ICONS = {
    "Castle": "🏰",
    "Forest": "🌲",
    "Ocean": "🌊",
    "Mountain": "⛰️",
    "Space": "🚀",
    "Jungle": "🌴",
    "Desert": "🏜️",
    "City": "🏙️"
}

def get_icon(item, icon_dict):
    """Get appropriate icon for item"""
    for key, icon in icon_dict.items():
        if key in item:
            return icon
    return "✨"

def create_story_tab():
    """Creates the UI for the Story Generator tab with guided step-by-step interface."""
    
    # State variables to track selections and current step
    selected_hero = gr.State("")
    selected_item = gr.State("")
    selected_setting = gr.State("")
    current_step = gr.State(1)  # 1=hero, 2=item, 3=setting, 4=ready
    
    # Progress indicator
    progress_indicator = gr.HTML(value="""
        <div class="progress-container">
            <div class="progress-step active" id="step1">1. 🦸‍♀️ Hero</div>
            <div class="progress-step" id="step2">2. ✨ Item</div>
            <div class="progress-step" id="step3">3. 🌍 World</div>
            <div class="progress-step" id="step4">4. 📖 Create!</div>
        </div>
    """)
    
    # Hero selection (initially visible)
    hero_section = gr.Column(visible=True)
    with hero_section:
        gr.Markdown("### **Who will be the hero of your story?**")
        gr.Markdown("*Pick your favorite character - they'll be the star of your adventure!*")
        with gr.Row():
            hero_buttons = []
            for hero in STORY_HEROES:
                icon = get_icon(hero, HERO_ICONS)
                btn = gr.Button(
                    f"{icon} {hero}", 
                    variant="secondary", 
                    size="lg",
                    elem_classes=["subject-button"]
                )
                hero_buttons.append(btn)
    
    # Item selection (initially hidden)
    item_section = gr.Column(visible=False)
    with item_section:
        gr.Markdown("### **What magical item will help your hero?**")
        gr.Markdown("*Choose a special object that will be important in your story!*")
        with gr.Row():
            item_buttons = []
            for item in STORY_ITEMS:
                icon = get_icon(item, ITEM_ICONS)
                btn = gr.Button(
                    f"{icon} {item}", 
                    variant="secondary", 
                    size="lg",
                    elem_classes=["theme-button"]
                )
                item_buttons.append(btn)
    
    # Setting selection (initially hidden)
    setting_section = gr.Column(visible=False)
    with setting_section:
        gr.Markdown("### **Where will your adventure take place?**")
        gr.Markdown("*Pick an exciting location for your story to unfold!*")
        with gr.Row():
            setting_buttons = []
            for setting in STORY_SETTINGS:
                icon = get_icon(setting, SETTING_ICONS)
                btn = gr.Button(
                    f"{icon} {setting}", 
                    variant="secondary", 
                    size="lg",
                    elem_classes=["age-button"]
                )
                setting_buttons.append(btn)
    
    # Summary and create button (initially hidden)
    summary_section = gr.Column(visible=False)
    with summary_section:
        gr.Markdown("### **🎉 Amazing! Here's your story setup:**")
        selection_summary = gr.Markdown("")
        create_btn = gr.Button("✨ Create My Amazing Story!", variant="primary", size="lg")
    
    # Loading animation (initially hidden)
    loading_html = gr.HTML(visible=False, value="""
        <div style="text-align: center; padding: 30px;">
            <div style="display: inline-block; font-size: 4em;" class="pulse-animation">✨</div>
            <div style="margin-top: 15px; font-size: 1.3em; color: #0ea5e9; font-weight: bold;">Crafting your magical story...</div>
            <div style="margin-top: 10px; font-style: italic; color: #666;">Our AI storyteller is weaving your adventure together!</div>
        </div>
    """)
    
    # Story output (initially hidden)
    story_output = gr.Textbox(
        label="📖 Your Amazing Story", 
        interactive=False, 
        lines=12, 
        visible=False,
        show_copy_button=True
    )
    
    # Audio controls for story (initially hidden)
    story_audio_section = gr.Column(visible=False)
    with story_audio_section:
        gr.Markdown("### 🔊 **Listen to your story!**")
        story_audio_button = gr.Button("🔊 Read Story Aloud", elem_classes=["audio-button"], variant="secondary")
        gr.Markdown("*Click the button above to hear your story read out loud!*")
    
    # Story illustration (initially hidden)
    story_image = gr.Image(label="🖼️ Your Story Illustration", visible=False)
    
    # AI affirmation section (initially hidden)
    ai_affirmation = gr.Column(visible=False)
    with ai_affirmation:
        gr.Markdown("### 🤖✨ **Amazing! You just created this story with Artificial Intelligence!**")
        gr.Markdown("You chose the characters and setting, and AI helped bring your imagination to life! 🎨")
        
        # Story sharing and rating section
        with gr.Row():
            with gr.Column():
                gr.Markdown("#### **Rate your story!**")
                with gr.Row():
                    for emoji in ["😍", "😄", "😊", "😐", "😕"]:
                        rating_btn = gr.Button(emoji, variant="secondary", size="sm")
            
            with gr.Column():
                gr.Markdown("#### **Share with family!**")
                share_btn = gr.Button("📤 Save Story", variant="secondary")
        
        # Fun facts about storytelling and AI
        with gr.Accordion("🤔 Want to know more about AI storytelling?", open=False):
            gr.Markdown("""
            **How does AI create stories?**
            - AI has read millions of stories to learn patterns and styles
            - It combines your choices with storytelling rules to create something new
            - Every story is unique based on what you choose!
            - AI can write in different styles - adventure, mystery, comedy, and more!
            
            **Fun storytelling tips:**
            - Try different combinations to see how your story changes
            - Think about what your character wants and what problems they face
            - The best stories have characters who grow and change
            """)
    
    new_story_btn = gr.Button("🎭 Create Another Story!", variant="secondary", visible=False)
    
    # Error handling section (initially hidden)
    error_section = gr.Column(visible=False)
    with error_section:
        gr.Markdown("### 😅 **Oops! Our storytelling magic got confused!**")
        gr.Markdown("Don't worry - even the best storytellers need a do-over sometimes!")
        retry_btn = gr.Button("🔄 Try Again", variant="primary")
    
    # Helper functions for guided experience
    def update_story_progress(step):
        """Update progress indicator for story creation"""
        steps_html = []
        icons = ["🦸‍♀️", "✨", "🌍", "📖"]
        labels = ["Hero", "Item", "World", "Create!"]
        
        for i in range(1, 5):
            if i < step:
                class_name = "progress-step completed"
                icon = "✅"
            elif i == step:
                class_name = "progress-step active"
                icon = icons[i-1]
            else:
                class_name = "progress-step"
                icon = icons[i-1]
            
            steps_html.append(f'<div class="{class_name}">{i}. {icon} {labels[i-1]}</div>')
        
        return f'<div class="progress-container">{"".join(steps_html)}</div>'
    
    def select_hero(hero_choice):
        """Handle hero selection and move to next step"""
        return (
            hero_choice,  # selected_hero
            2,  # current_step (move to item selection)
            update_story_progress(2),  # progress_indicator
            gr.update(visible=False),  # hero_section
            gr.update(visible=True),   # item_section
            gr.update(visible=False),  # setting_section
            gr.update(visible=False),  # summary_section
            gr.update(visible=False)   # error_section
        )
    
    def select_item(item_choice, hero):
        """Handle item selection and move to next step"""
        return (
            item_choice,  # selected_item
            3,  # current_step (move to setting selection)
            update_story_progress(3),  # progress_indicator
            gr.update(visible=False),  # hero_section
            gr.update(visible=False),  # item_section
            gr.update(visible=True),   # setting_section
            gr.update(visible=False),  # summary_section
            gr.update(visible=False)   # error_section
        )
    
    def select_setting(setting_choice, hero, item):
        """Handle setting selection and show summary"""
        hero_icon = get_icon(hero, HERO_ICONS)
        item_icon = get_icon(item, ITEM_ICONS)
        setting_icon = get_icon(setting_choice, SETTING_ICONS)
        
        summary_text = f"""
**{hero_icon} Hero:** {hero}  
**{item_icon} Magical Item:** {item}  
**{setting_icon} World:** {setting_choice}

**Get ready for an epic adventure!** 🌟
        """
        return (
            setting_choice,  # selected_setting
            4,  # current_step (ready to create)
            update_story_progress(4),  # progress_indicator
            gr.update(visible=False),  # hero_section
            gr.update(visible=False),  # item_section
            gr.update(visible=False),  # setting_section
            gr.update(visible=True),   # summary_section
            summary_text,  # selection_summary
            gr.update(visible=False)   # error_section
        )
    
    def generate_story(hero, item, setting):
        """Generate the story and show loading/result with enhanced error handling"""
        try:
            # Hide summary section and show loading
            yield (
                gr.update(visible=False),    # summary_section
                gr.update(visible=True),     # loading
                gr.update(visible=False),    # story
                gr.update(visible=False),    # story_audio_section
                gr.update(visible=False),    # story_image
                gr.update(visible=False),    # ai_affirmation
                gr.update(visible=False),    # new story button
                gr.update(visible=False)     # error_section
            )
            
            # Generate story
            story_text, image_path = safe_generate_story(hero, item, setting)
            
            # Show result with AI affirmation and optional image
            show_image = image_path is not None
            yield (
                gr.update(visible=False),    # summary_section (keep hidden)
                gr.update(visible=False),    # loading
                gr.update(value=story_text, visible=True),  # story
                gr.update(visible=True),     # story_audio_section
                gr.update(value=image_path, visible=show_image),    # story_image
                gr.update(visible=True),     # ai_affirmation
                gr.update(visible=True),     # new story button
                gr.update(visible=False)     # error_section
            )
        except Exception as e:
            # Child-friendly error message
            print(f"Error in generate_story: {str(e)}")
            yield (
                gr.update(visible=False),    # summary_section
                gr.update(visible=False),    # loading
                gr.update(visible=False),    # story
                gr.update(visible=False),    # story_audio_section
                gr.update(visible=False),    # story_image
                gr.update(visible=False),    # ai_affirmation
                gr.update(visible=False),    # new story button
                gr.update(visible=True)      # error_section
            )
    
    def reset_story():
        """Reset everything back to step 1"""
        return (
            "",  # selected_hero
            "",  # selected_item
            "",  # selected_setting
            1,   # current_step
            update_story_progress(1),  # progress_indicator
            gr.update(visible=True),   # hero_section
            gr.update(visible=False),  # item_section
            gr.update(visible=False),  # setting_section
            gr.update(visible=False),  # summary_section
            "",  # selection_summary
            gr.update(visible=False, value=""),  # story_output
            gr.update(visible=False),  # story_audio_section
            gr.update(visible=False),  # story_image
            gr.update(visible=False),  # ai_affirmation
            gr.update(visible=False),  # new_story_btn
            gr.update(visible=False)   # error_section
        )
    
    def handle_story_audio():
        """Handle story audio playback - placeholder for now"""
        return gr.update(value="🔊 Audio feature coming soon! For now, you can read your story out loud together.")
    
    def handle_story_rating(rating):
        """Handle story rating - placeholder for now"""
        return gr.update(value=f"Thanks for rating our story {rating}! We love your feedback.")
    
    def handle_story_share():
        """Handle story sharing - placeholder for now"""
        return gr.update(value="Story saved! You can copy the text above to share with family and friends.")
    
    # Event Listeners
    
    # Connect hero buttons
    for i, btn in enumerate(hero_buttons):
        btn.click(
            fn=lambda i=i: select_hero(STORY_HEROES[i]),
            outputs=[selected_hero, current_step, progress_indicator,
                    hero_section, item_section, setting_section, summary_section, error_section]
        )
    
    # Connect item buttons
    for i, btn in enumerate(item_buttons):
        btn.click(
            fn=lambda hero, i=i: select_item(STORY_ITEMS[i], hero),
            inputs=[selected_hero],
            outputs=[selected_item, current_step, progress_indicator,
                    hero_section, item_section, setting_section, summary_section, error_section]
        )
    
    # Connect setting buttons
    for i, btn in enumerate(setting_buttons):
        btn.click(
            fn=lambda hero, item, i=i: select_setting(STORY_SETTINGS[i], hero, item),
            inputs=[selected_hero, selected_item],
            outputs=[selected_setting, current_step, progress_indicator,
                    hero_section, item_section, setting_section, summary_section, 
                    selection_summary, error_section]
        )
    
    # Connect create story button
    create_btn.click(
        fn=generate_story,
        inputs=[selected_hero, selected_item, selected_setting],
        outputs=[summary_section, loading_html, story_output, story_audio_section, 
                story_image, ai_affirmation, new_story_btn, error_section]
    )
    
    # Connect new story button
    new_story_btn.click(
        fn=reset_story,
        outputs=[selected_hero, selected_item, selected_setting, current_step, progress_indicator,
                hero_section, item_section, setting_section, summary_section, 
                selection_summary, story_output, story_audio_section, story_image, 
                ai_affirmation, new_story_btn, error_section]
    )
    
    # Connect retry button
    retry_btn.click(
        fn=reset_story,
        outputs=[selected_hero, selected_item, selected_setting, current_step, progress_indicator,
                hero_section, item_section, setting_section, summary_section, 
                selection_summary, story_output, story_audio_section, story_image, 
                ai_affirmation, new_story_btn, error_section]
    )
    
    # Connect audio button (placeholder functionality)
    story_audio_button.click(
        fn=handle_story_audio,
        outputs=[story_output]
    )
    
    # Connect share button (placeholder functionality)
    share_btn.click(
        fn=handle_story_share,
        outputs=[story_output]
    )