from flet import *

def InputetextField(text, hide):
    return Container(
        alignment=alignment.center,
        content=TextField(
            height=48,
            width=300,
            text_size=12,
            color="black",
            border_radius=6,
            bgcolor="#f0f3f6",
            border_color="transparent",
            filled=True,
            cursor_color="black",
            cursor_width=1,
            hint_text=text,
            hint_style=TextStyle(size=11, color="black"),
            password=hide,
        ),
    )


def SignInOption(btn_name, func):
    return Container(
        content=ElevatedButton(
            on_click=func,
            content=Text(
                btn_name,
                size=11,
                weight="bold",
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=8),
                },
                color={
                    "":"white",
                },
            ),
            height=42,
            width=300,
        ),
    )