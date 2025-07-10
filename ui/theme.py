# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (c) 2025 Jack Pollard

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

# Custom CSS for multipage layout with production enhancements
multipage_css = """
/* Core Page Styling */
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

/* Progress Indicator Styling */
.progress-container {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
    padding: 15px;
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(14, 165, 233, 0.1);
    border: 2px solid #bae6fd;
}

.progress-step {
    text-align: center;
    padding: 10px 16px;
    border-radius: 25px;
    font-size: 16px;
    color: #64748b;
    font-weight: bold;
    background: white;
    transition: all 0.3s ease;
    border: 2px solid transparent;
    min-width: 120px;
}

.progress-step.active {
    background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
    color: white;
    box-shadow: 0 4px 12px rgba(14, 165, 233, 0.4);
    transform: scale(1.05);
    border: 2px solid #0284c7;
}

.progress-step.completed {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}

/* Enhanced Subject/Theme Button Styling */
.subject-button, .theme-button, .age-button {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border: 3px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px;
    margin: 8px;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    min-height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1em;
    font-weight: 600;
    text-align: center;
}

.subject-button:hover, .theme-button:hover, .age-button:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(14, 165, 233, 0.2);
    border-color: #0ea5e9;
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
}

.subject-button.selected, .theme-button.selected, .age-button.selected {
    background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
    color: white;
    border-color: #0284c7;
    box-shadow: 0 8px 25px rgba(14, 165, 233, 0.4);
}

/* Custom Age Button Styling */
.custom-age-btn {
    background: linear-gradient(135deg, #fef3c7 0%, #fbbf24 100%);
    border: 3px solid #f59e0b;
    border-radius: 20px;
    padding: 16px;
    margin: 6px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(245, 158, 11, 0.2);
    min-width: 100px;
    min-height: 90px;
}

.custom-age-btn:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 8px 20px rgba(245, 158, 11, 0.3);
    background: linear-gradient(135deg, #fed7aa 0%, #fb923c 100%);
    border-color: #ea580c;
}

.age-number {
    font-size: 2em;
    font-weight: bold;
    color: #92400e;
    margin-bottom: 4px;
}

.age-label {
    font-size: 0.9em;
    color: #b45309;
    font-weight: 600;
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
    border-radius: 12px;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.gr-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Audio Button Styling */
.audio-button {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white;
    border: none;
    border-radius: 50px;
    padding: 12px 20px;
    font-size: 1.1em;
    font-weight: bold;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    transition: all 0.3s ease;
}

.audio-button:hover {
    background: linear-gradient(135deg, #059669 0%, #047857 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4);
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

@keyframes pulse {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.1); opacity: 0.7; }
    100% { transform: scale(1); opacity: 1; }
}

.pulse-animation {
    animation: pulse 1.5s infinite;
}

/* Mobile responsiveness improvements */
@media (max-width: 768px) {
    .gr-button {
        font-size: 1em !important;
        padding: 12px !important;
        min-height: 50px !important;
        margin: 6px 0 !important;
    }
    
    .gr-row {
        flex-direction: column !important;
    }
    
    .page-title h1 {
        font-size: 1.8em !important;
    }
    
    .page-subtitle {
        font-size: 1.2em !important;
    }
    
    .progress-container {
        flex-direction: column !important;
        gap: 10px !important;
    }
    
    .progress-step {
        min-width: auto !important;
        width: 100% !important;
    }
    
    .subject-button, .theme-button, .age-button {
        min-height: 60px !important;
        font-size: 1em !important;
        padding: 16px !important;
    }
}

/* Reduce animations for performance on low-end devices */
@media (prefers-reduced-motion: reduce) {
    .loading-bounce, .pulse-animation, .gr-button:hover {
        animation: none !important;
        transform: none !important;
    }
}

/* Accessibility improvements */
.gr-button:focus {
    outline: 3px solid #0ea5e9;
    outline-offset: 2px;
}

/* High contrast mode support */
@media (prefers-contrast: high) {
    .progress-step {
        border: 3px solid currentColor;
    }
    
    .subject-button, .theme-button, .age-button {
        border: 3px solid currentColor;
    }
}
"""