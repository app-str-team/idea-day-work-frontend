import random
from math import pi
import time

import flet
from flet import Container, ElevatedButton, Page, Stack, colors, Text, Column

from flet import *

class AnimationControl(flet.UserControl):

    def loading_animation(self):

        size = 15
        gap = 1
        duration = 2000

        c1 = colors.PINK_500
        c2 = colors.AMBER_500
        c3 = colors.LIGHT_GREEN_500
        c4 = colors.DEEP_PURPLE_500
        c5 = colors.BROWN_400
        c6 = colors.GREEN_ACCENT_200
        c7 = colors.CYAN_700

        all_colors = [
            colors.AMBER_400,
            colors.AMBER_ACCENT_400,
            colors.BLUE_400,
            colors.BROWN_400,
            colors.CYAN_700,
            colors.DEEP_ORANGE_500,
            colors.CYAN_500,
            colors.INDIGO_600,
            colors.ORANGE_ACCENT_100,
            colors.PINK,
            colors.RED_600,
            colors.GREEN_400,
            colors.GREEN_ACCENT_200,
            colors.TEAL_ACCENT_200,
            colors.LIGHT_BLUE_500,
        ]

        parts = [
            # I
            (0, 0, c1),
            (0, 4, c1),
            (1, 0, c1),
            (1, 1, c1),
            (1, 2, c1),
            (1, 3, c1),
            (1, 4, c1),
            (2, 0, c1),
            (2, 4, c1),
            # D
            (4, 0, c2),
            (4, 1, c2),
            (4, 2, c2),
            (4, 3, c2),
            (4, 4, c2),
            (5, 0, c2),
            (5, 4, c2),
            (6, 1, c2),
            (6, 2, c2),
            (6, 3, c2),
            # E
            (8, 0, c3),
            (9, 0, c3),
            (10, 0, c3),
            (8, 1, c3),
            (8, 2, c3),
            (9, 2, c3),
            (10, 2, c3),
            (8, 3, c3),
            (8, 4, c3),
            (9, 4, c3),
            (10, 4, c3),
            # A
            (12, 1, c4),
            (12, 2, c4),
            (12, 3, c4),
            (12, 4, c4),
            (13, 0, c4),
            (13, 2, c4),
            (14, 1, c4),
            (14, 2, c4),
            (14, 3, c4),
            (14, 4, c4),
            # D
            (2, 6, c5),
            (2, 7, c5),
            (2, 8, c5),
            (2, 9, c5),
            (2, 10, c5),
            (3, 6, c5),
            (3, 10, c5),
            (4, 7, c5),
            (4, 8, c5),
            (4, 9, c5),
            # A
            (6, 7, c6),
            (6, 8, c6),
            (6, 9, c6),
            (6, 10, c6),
            (7, 6, c6),
            (7, 8, c6),
            (8, 7, c6),
            (8, 8, c6),
            (8, 9, c6),
            (8, 10, c6),
            # Y
            (10, 6, c7),
            (10, 7, c7),
            (11, 8, c7),
            (11, 9, c7),
            (11, 10, c7),
            (12, 6, c7),
            (12, 7, c7),
            # A
            (2, 13, c5),
            (2, 14, c5),
            (2, 15, c5),
            (2, 16, c5),
            (3, 12, c5),
            (3, 14, c5),
            (4, 13, c5),
            (4, 14, c5),
            (4, 15, c5),
            (4, 16, c5),
            # P
            (6, 12, c6),
            (6, 13, c6),
            (6, 14, c6),
            (6, 15, c6),
            (6, 16, c6),
            (7, 12, c6),
            (7, 14, c6),
            (8, 12, c6),
            (8, 13, c6),
            (8, 14, c6),
            # P
            (10, 12, c6),
            (10, 13, c6),
            (10, 14, c6),
            (10, 15, c6),
            (10, 16, c6),
            (11, 12, c6),
            (11, 14, c6),
            (12, 12, c6),
            (12, 13, c6),
            (12, 14, c6),
        ]

        width = 16 * (size + gap)
        height = 18 * (size + gap)

        canvas = Stack(
            width=width,
            height=height,
            animate_scale=duration,
            animate_opacity=duration,
        )

        # spread parts randomly
        for i in range(len(parts)):
            canvas.controls.append(
                Container(
                    animate=duration,
                    animate_position=duration,
                    animate_rotation=duration,
                )
            )

        def randomize():
            random.seed()
            for i in range(len(parts)):
                c = canvas.controls[i]
                part_size = random.randrange(int(size / 2), int(size * 3))
                c.left = random.randrange(0, width)
                c.top = random.randrange(0, height)
                c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
                c.width = part_size
                c.height = part_size
                c.border_radius = random.randrange(0, int(size / 2))
                c.rotate = random.randrange(0, 90) * 2 * pi / 360
            canvas.scale = 1
            canvas.opacity = 0.5
            #go_button.visible = True
            #again_button.visible = False
            self.page.update()

        def assemble():
            i = 0
            for left, top, bgcolor in parts:
                c = canvas.controls[i]
                c.left = left * (size + gap)
                c.top = top * (size + gap)
                c.bgcolor = bgcolor
                c.width = size
                c.height = size
                c.border_radius = 5
                c.rotate = 0
                i += 1
            canvas.scale = 1
            canvas.opacity = 1
            #go_button.visible = False
            #again_button.visible = True
            self.page.update()

        #go_button = ElevatedButton("Go!", on_click=assemble)
        #again_button = ElevatedButton("Again!", on_click=randomize)

        #randomize(None)

        welcome_label = Text("WELCOME \n TO", size=50, weight="w500", text_align="center", color="#1976D2",
                            font_family="Forte")

        self.page.horizontal_alignment = "center"
        self.page.vertical_alignment = "center"
        self.page.spacing = 30
        self.page.add(welcome_label, canvas)
        boolAnimation = True
        # while boolAnimation:
        randomize()
        time.sleep(3)  # Adjust the sleep duration as needed
        assemble()
        time.sleep(3)
            

    def __init__(self,page):
        super().__init__()
        self.page = page

    def build(self):
        self.display_task = self.loading_animation()

        self.display_view = flet.Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task
            ],
        )


        return Column(
            width=400,
            auto_scroll=True,
            controls=[self.display_view])

#def main(page: Page):
#    AnimationControl(page).build()

# Run the app
#flet.app(main,view=AppView.WEB_BROWSER)
