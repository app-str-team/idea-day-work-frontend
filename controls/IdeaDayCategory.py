import flet
from flet import *
from controls import IdeaDayTeam

import requests

class IdeaDayCategory(UserControl):
    # def __init__(self, task_name, start):
    #     super().__init__()
    #     self.completed = False
    #     self.visible = False
    #     self.task_name = task_name
    #     self.start = start
    #     self.end = 40

    techBiz_Task_List =[]
    productInnovation_Task_List = []
    processInnovation_Task_List = []
    customerDelight_Task_List = []

    def getTaskList(self):
        return self.Task_List

    def __init__(self, task_name, laskList):
        super().__init__()
        self.completed = False
        self.visible = False
        self.task_name = task_name
        self.Task_List = laskList
        if(task_name == "TECHBIZ CATEGORY"):
            IdeaDayCategory.techBiz_Task_List  =  laskList
        if (task_name == "PRODUCT INNOVATION"):
            IdeaDayCategory.productInnovation_Task_List = laskList
        if (task_name == "PROCESS INNOVATION"):
            IdeaDayCategory.processInnovation_Task_List = laskList
        if (task_name == "CUSTOMER DELIGHT"):
            IdeaDayCategory.customerDelight_Task_List = laskList
        self.start = 0



    def example(self):
        def on_click(e):
            step = e.page.controls[0].controls[0].controls[0]
            step.controls[0].visible = False
            step.controls[1].visible = False
            IdeaDayParameter = []
            if(step.controls[2].controls != []):
                step.controls[2].controls.pop()
            if (e.control.data == "techbiz"):
                IdeaDayParameter = IdeaDayCategory.techBiz_Task_List[e.control.tooltip]
            if (e.control.data == "visionary_champs"):
                IdeaDayParameter = IdeaDayCategory.productInnovation_Task_List[e.control.tooltip]
            if (e.control.data == "efficiency_champs"):
                IdeaDayParameter = IdeaDayCategory.processInnovation_Task_List[e.control.tooltip]
            if (e.control.data == "customer_delight"):
                IdeaDayParameter = IdeaDayCategory.customerDelight_Task_List[e.control.tooltip]

            step.controls[2].controls.append(IdeaDayTeam.IdeaDayTeam(IdeaDayParameter))
            step.controls[2].update()
            step.controls[2].visible = True
            step.update()
            print(
                "I am working"
            )
            e.page.update()

        images = flet.GridView(
            height=400,
            width=400,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            auto_scroll=True,
            spacing=5,
            run_spacing=5,
        )

        for i in self.Task_List:
            images.controls.append(flet.Container(
                content=flet.Stack(
                    [
                        flet.Image(
                            src=i[0],
                            fit=flet.ImageFit.NONE,
                            repeat=flet.ImageRepeat.NO_REPEAT,
                            border_radius=flet.border_radius.all(10),
                        ),
                        flet.Row(
                            [
                                # flet.Text(
                                #     "Image title",
                                #     color=flet.colors.WHITE,
                                #     bgcolor=flet.colors.GREEN_700,
                                #     size=30,
                                #     weight = flet.FontWeight.BOLD,
                                #     no_wrap=False,
                                #     italic = True,
                                #     max_lines=2,
                                #     width=120,
                                # )
                                flet.Text(
                                    spans=[
                                        flet.TextSpan(
                                            i[1],
                                            flet.TextStyle(
                                                size=25,
                                                weight=flet.FontWeight.BOLD,
                                                foreground=flet.Paint(
                                                    gradient=flet.PaintLinearGradient(
                                                        (0, 20), (150, 20), [flet.colors.RED, flet.colors.YELLOW]
                                                    )
                                                ),
                                            ),
                                        ),
                                    ],
                                    width=120,
                                )
                            ],
                            alignment=flet.MainAxisAlignment.CENTER,
                            top=20,
                            left=10
                        ),

                    ]
                ),
                tooltip=i[2],
                #url=i[5],
                data=i[5],
                on_click=on_click
            ))
        # else:
        #     for i in range(10, 20):
        #         images.controls.append(flet.Container(
        #            content= flet.Image(
        #                 src=f"https://picsum.photos/150/150?{i}",
        #                 fit=flet.ImageFit.NONE,
        #                 repeat=flet.ImageRepeat.NO_REPEAT,
        #                 border_radius=flet.border_radius.all(10),
        #             ),
        #             on_click=on_click
        #         ))

        return images

    def on_click(e):
        pass
    def build(self):
        self.display_task = self.example()
        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task
            ],
        )

        return Column(controls=[self.display_view])