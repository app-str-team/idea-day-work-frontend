from flet import *
from controls import navbar
from view import ShowMenu


def _view_(first_name:str, last_name:str):
    return View(
        '/home',
        bgcolor="white54",
        controls=[
            Column(
                expand=True,
                controls=[
                    Row(
                        expand=True,
                        controls=[
                            Column(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Container(
                                        margin=10,
                                        bgcolor="#1d1d1d",
                                        width=60,
                                        expand=True,
                                        animate=animation.Animation(350,"decelerate"),
                                        on_hover= lambda e: ShowMenu(e),
                                        content=navbar.ModernNavbar(),
                                    )
                                ],
                            ),
                            VerticalDivider(width=60, color='transparent'),
                            Column(
                                expand=True,
                                alignment=MainAxisAlignment.START,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Divider(height=30, color='transparent'),
                                ]
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )