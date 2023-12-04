import flet
from flet import *
import requests
from main import _moduleList

class IdeaDayTeam(UserControl):
    def loadTeam(self):
        names = self.TeadData[3]
        def on_backarrow_clicked(e):
            step = e.page.controls[0].controls[0].controls[0]
            step.controls[0].visible = True
            step.controls[1].visible = True
            step.controls[2].visible = False

            step.update()
        def on_submit_opinion_clicked(e):
            print ("on_submit_opinion_clicked")
            e.page.views.clear()
            e.page.views.append(
            _moduleList['/postComments'].loader.load_module()._view_(e.page))
            e.page.update()
            
        return Column(controls=[
            Container(
                width=300,
                content=Text(
                    self.TeadData[1],
                    size=30,
                    color="#000000",
                    weight="w700",
                    text_align="center",
                    font_family="Calisto MT"
                )),
            Container(
                width=300,
                margin=margin.only(left=30, right=30, top=10),
                bgcolor="#D3D3D3",
                border_radius=10,
                padding=10,
                content=Column(
                    controls=[
                        Text(
                            "Synopsis",
                            size=16,
                            color="#333333",
                            weight="w700",
                            text_align="center",
                        ),
                        Text(
                            self.TeadData[4],
                            size=12,
                            color="#333333",
                            text_align="LEFT"
                        ),
                    ]
                )
            ),
            Container(
                width=300,
                height=75,
                margin=margin.only(left=30, right=30, top=10),
                bgcolor="#D3D3D3",
                border_radius=10,
                padding=10,
                content=Column(
                    controls=[
                        Text(
                            "Video Link",
                            size=16,
                            color="#333333",
                            weight="w700",
                            text_align="center",
                        ),
                        Text(
                            disabled=False,
                            spans=[
                                TextSpan(
                                    "Visit our website",
                                    TextStyle(decoration=TextDecoration.UNDERLINE, color=colors.BLUE),
                                    url="https://www.youtube.com/watch?v=fBbKiXVun4U"
                                )
                            ]
                        )
                    ]
                )
            ),
            Container(
                width=300,
                margin=margin.only(left=30, right=30, top=10),
                bgcolor="#D3D3D3",
                border_radius=10,
                padding=10,
                content=Column(
                    controls=[
                        Text(
                            "Team Members",
                            size=16,
                            color="#333333",
                            weight="w700",
                            text_align="center",
                        ),
                        *[
                            Container(
                                width=250,  # Adjust the width as needed
                                margin=margin.only(left=20, top=0, bottom=0),
                                content=Row(
                                    controls=[
                                        Text("•", size=12, color="#333333"),  # Bullet point
                                        Text(name, size=12, color="#333333"),
                                    ]
                                )
                            )
                            for name in names
                        ]
                    ]
                )
            ),
            Container(
                width=260,
                margin=margin.only(left=30, right=20, top=10),
                content=ElevatedButton(
                    "Submit your vote here",
                    width=300,
                    height=40,
                    on_click=on_submit_opinion_clicked,
                    style=ButtonStyle(
                        bgcolor=colors.BLACK,
                        color=colors.WHITE,
                        shape={
                            MaterialState.DEFAULT: RoundedRectangleBorder(radius=5),
                            MaterialState.HOVERED: RoundedRectangleBorder(radius=5),
                            MaterialState.FOCUSED: RoundedRectangleBorder(radius=5)
                        },
                        padding=10,
                    )
                )
            ),
            Container(
                content=IconButton(
                    icon=icons.ARROW_BACK,
                    icon_color="BLUE_50",
                    icon_size=20,
                    tooltip="Back Home",
                    on_click=on_backarrow_clicked
                ),
                bgcolor=colors.TEAL,
                padding=5,
            )],
            scroll=ScrollMode.ALWAYS
        )
    def __init__(self, task_name):
        super().__init__()
        self.TeadData = task_name


    def build(self):
        self.display_task = self.loadTeam()
        self.visible = True
        return Column(controls=[self.display_task],scroll=ScrollMode.ALWAYS)

