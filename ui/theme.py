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
        )

kids_theme = KidsTheme()