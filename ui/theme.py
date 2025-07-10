# ui/theme.py
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes

class KidsTheme(Base):
    def __init__(self):
        super().__init__(
            primary_hue=colors.sky,
            secondary_hue=colors.amber,
            neutral_hue=colors.gray,
            text_size=sizes.text_lg,
            spacing_size=sizes.spacing_lg,
            radius_size=sizes.radius_lg,
            font=(fonts.GoogleFont("Nunito"), "ui-sans-serif", "sans-serif"),
        )
        # Custom overrides
        self.set(
            # Component-specific overrides
            button_primary_background_fill="*primary_500",
            button_primary_background_fill_hover="*primary_400",
            button_primary_text_color="white",
            # Page layout improvements
            layout_gap="*spacing_lg",
            panel_background_fill="*neutral_50",
        )

kids_theme = KidsTheme()

# Custom CSS for multipage layout
multipage_css = """
.page-title h1 {
    text-align: center;
    color: #0369a1;
    font-size: 2.5em;
    margin-bottom: 0.5em;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

.page-subtitle {
    text-align: center;
    color: #64748b;
    font-size: 1.3em;
    margin-bottom: 2em;
    font-weight: 500;
}

/* Navigation styling */
.gradio-tabs {
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Style the first tab (KidsAI) as a logo */
.gradio-tabs .tab-nav button:first-child {
    background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 100%);
    color: white;
    font-weight: bold;
    font-size: 1.1em;
    border: none;
    margin-right: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
    transition: all 0.3s ease;
}

.gradio-tabs .tab-nav button:first-child:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
}

/* Make the logo tab slightly larger */
.gradio-tabs .tab-nav button:first-child {
    padding: 8px 16px;
    min-width: 120px;
}

/* Better spacing for content */
.main-content {
    padding: 2em;
    max-width: 1200px;
    margin: 0 auto;
}

/* Enhanced button styling */
.gr-button {
    transition: all 0.3s ease;
    border-radius: 8px;
    font-weight: 600;
}

.gr-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Fun animation for loading */
@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-10px);
    }
    60% {
        transform: translateY(-5px);
    }
}

.loading-bounce {
    animation: bounce 2s infinite;
}
"""