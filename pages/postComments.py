from flet import *
from controls import inputTextField
from view import PostJudgeScore,homePage

def _view_():
    return View(
        "/postComments",
        bgcolor='#fafafa',
        horizontal_alignment=CrossAxisAlignment.CENTER,
        vertical_alignment=MainAxisAlignment.CENTER,
        controls=[
            Column(
                controls=[
                        Container(
                        width=350,
                        height=650,
                        border_radius=8,
                        bgcolor="#ffffff",
                        border=border.all(3,"#dbdbdb"),
                        alignment=alignment.center,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=15, color="transparent"),
                                Text(
                                    "JUDGEMENT FORM",
                                    size=21,
                                    weight="w600",
                                    color="Black"
                                ),
                                Text(
                                    "Fill out the form below to give the Score and comments for Idea's",
                                    size=12,
                                    weight="w500",
                                    color="Black",
                                    text_align="center"
                                    
                                ),
                                Divider(height=11, color="transparent"),
                                Column(
                                    spacing=5,
                                    controls=[
                                        inputTextField.InputtextField("Idea Pitch","Enter the Score between 1-15"),
                                        inputTextField.InputtextField("Efficiency value","Enter the Score between 1-35"),
                                        inputTextField.InputtextField("Feature Scope","Enter the Score between 1-10"),
                                        inputTextField.InputtextField("Working Model","Enter the Score between 1-30"),
                                        inputTextField.InputtextField("Presentation","Enter the Score between 1-10"),
                                        inputTextField.MultitextField("Comment","Enter Your comment here"),
                                    ],
                                ),

                                # Divider(height=5, color="transparent"),

                                inputTextField.SignInOption( "POST JUDGEMENT", lambda e: PostJudgeScore(e)),
                                Divider(height=5, color="transparent"),
                                inputTextField.SignInOption( "BCAK", lambda e: homePage(e)),
                                Divider(height=5, color="transparent"),
                            ],
                        ),
                    ),
                ],
            ),
        ],
    )
