from flet import *
from controls import navbar
from view import ShowMenu
from controls import IdeaDayApp

'''
def _view_(page : Page):
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
                                    ),
                                ],
                            ),
                            VerticalDivider(width=60, color='transparent'),
                            Column(
                                expand=True,
                                alignment=MainAxisAlignment.START,
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                controls=[
                                    Divider(height=30, color='transparent'),

                                    Divider(height=30, color="transparent"),
                                    Column(
                                        expand=True, scroll="hidden"
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
'''   

def _view_(page : Page):
    control = IdeaDayApp.IdeaDayApp()
    page.add(control)
    return View(    
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment = CrossAxisAlignment.CENTER,
        controls=[control]
    )