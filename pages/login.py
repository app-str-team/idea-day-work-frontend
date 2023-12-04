
from flet import *
from controls import inputText
from view import ChangeRoute,logInUser


def _view_(page : Page):
    return View(
        "/login",
        bgcolor='#fafafa',
        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER,
        controls=[
            Column(
                controls=[
                        Container(
                        width=350,
                        height=500,
                        border_radius=8,
                        bgcolor="#ffffff",
                        border=border.all(3,"#dbdbdb"),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=20, color="transparent"),
                                Text(
                                    "Login Form",
                                    size=26,
                                    weight="w600",
                                    color="Black"
                                ),
                                Text(
                                    "Use the form below to log into your account",
                                    size=12,
                                    weight="w400",
                                    color="Black"
                                ),
                                Divider(height=40, color="transparent"),
                                Column(
                                    spacing=5,
                                    controls=[
                                        inputText.InputetextField("Email", False, False),
                                        inputText.InputetextField("Password", True, True),
                                    ],
                                ),
                                Row(
                                    width=300,
                                    alignment=MainAxisAlignment.END,
                                    controls=[
                                        Text(
                                            "Forgot Password",
                                            color="black",
                                            weight="bold",
                                            size=10,
                                        ),
                                    ],
                                ),
                                Divider(height=5, color="transparent"),

                                inputText.SignInOption( "Log In", lambda e: logInUser(e) ),
                                Divider(height=60, color="transparent"),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    spacing=4,
                                    controls=[
                                        Text(
                                            "Don't have an account",
                                            color="black",
                                            size=10,
                                            weight='bold',
                                        ),
                                        Container(
                                            on_click= lambda e: ChangeRoute(e, "/register"),
                                            content=Text(
                                                "Sign In",
                                                color="blue900",
                                                size=10,
                                                weight="bold",
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ],
    )