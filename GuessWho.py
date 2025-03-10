import flet as ft
from itertools import cycle

def main(page: ft.Page):

#-------------------------------------------------------------------#
#card 1-------------------------------------------------------------#

    card1imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/alexcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card1img = card1imglist[0]

    def card1imgfunc(e):
        if e.control.image_src == card1imglist[1]:
            e.control.image_src = card1imglist[0]
        else:
            e.control.image_src = card1imglist[1]
        page.update()

    card1 = ft.Container(margin=10,
                         padding=10,
                         height=150,
                         width=100,
                         image_src=card1img,
                         on_click=card1imgfunc)

#-------------------------------------------------------------------#
#card 2-------------------------------------------------------------#

    card2imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/alfredcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card2img = card2imglist[0]

    def card2imgfunc(e):
        if e.control.image_src == card2imglist[1]:
            e.control.image_src = card2imglist[0]
        else:
            e.control.image_src = card2imglist[1]
        page.update()

    card2 = ft.Container(margin=10,
                         padding=10,
                         height=150,
                         width=100,
                         image_src=card2img,
                         on_click=card2imgfunc)

#-------------------------------------------------------------------#
#card 3-------------------------------------------------------------#

    card3imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/anitacard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card3img = card3imglist[0]

    def card3imgfunc(e):
        if e.control.image_src == card3imglist[1]:
            e.control.image_src = card3imglist[0]
        else:
            e.control.image_src = card3imglist[1]
        page.update()

    card3 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card3img,
                         on_click=card3imgfunc)

#-------------------------------------------------------------------#
#card 4-------------------------------------------------------------#

    card4imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/annecard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card4img = card4imglist[0]

    def card4imgfunc(e):
        if e.control.image_src == card4imglist[1]:
            e.control.image_src = card4imglist[0]
        else:
            e.control.image_src = card4imglist[1]
        page.update()

    card4 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card4img,
                         on_click=card4imgfunc)

#-------------------------------------------------------------------#
#card 5-------------------------------------------------------------#

    card5imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/bernardcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card5img = card5imglist[0]

    def card5imgfunc(e):
        if e.control.image_src == card5imglist[1]:
            e.control.image_src = card5imglist[0]
        else:
            e.control.image_src = card5imglist[1]
        page.update()

    card5 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card5img,
                         on_click=card5imgfunc)

#-------------------------------------------------------------------#
#card 6-------------------------------------------------------------#

    card6imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/billcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card6img = card6imglist[0]

    def card6imgfunc(e):
        if e.control.image_src == card6imglist[1]:
            e.control.image_src = card6imglist[0]
        else:
            e.control.image_src = card6imglist[1]
        page.update()

    card6 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card6img,
                         on_click=card6imgfunc)

#-------------------------------------------------------------------#
#card 7-------------------------------------------------------------#

    card7imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/charlescard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card7img = card7imglist[0]

    def card7imgfunc(e):
        if e.control.image_src == card7imglist[1]:
            e.control.image_src = card7imglist[0]
        else:
            e.control.image_src = card7imglist[1]
        page.update()

    card7 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card7img,
                         on_click=card7imgfunc)

#-------------------------------------------------------------------#
#card 8-------------------------------------------------------------#



    card8imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/clairecard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card8img = card8imglist[0]

    def card8imgfunc(e):
        if e.control.image_src == card8imglist[1]:
            e.control.image_src = card8imglist[0]
        else:
            e.control.image_src = card8imglist[1]
        page.update()

    card8 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card8img,
                         on_click=card8imgfunc)
    
#-------------------------------------------------------------------#
#card 9-------------------------------------------------------------#

    card9imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/davidcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card9img = card9imglist[0]

    def card9imgfunc(e):
        if e.control.image_src == card9imglist[1]:
            e.control.image_src = card9imglist[0]
        else:
            e.control.image_src = card9imglist[1]
        page.update()

    card9 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card9img,
                         on_click=card9imgfunc)
    
#-------------------------------------------------------------------#
#card 10-------------------------------------------------------------#

    card10imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/ericcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card10img = card10imglist[0]

    def card10imgfunc(e):
        if e.control.image_src == card10imglist[1]:
            e.control.image_src = card10imglist[0]
        else:
            e.control.image_src = card10imglist[1]
        page.update()

    card10 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card10img,
                         on_click=card10imgfunc)
    
#-------------------------------------------------------------------#
#card 11-------------------------------------------------------------#

    card11imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/franscard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card11img = card11imglist[0]

    def card11imgfunc(e):
        if e.control.image_src == card11imglist[1]:
            e.control.image_src = card11imglist[0]
        else:
            e.control.image_src = card11imglist[1]
        page.update()

    card11 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card11img,
                         on_click=card11imgfunc)
    
#-------------------------------------------------------------------#
#card 12-------------------------------------------------------------#

    card12imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/georgecard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card12img = card12imglist[0]

    def card12imgfunc(e):
        if e.control.image_src == card12imglist[1]:
            e.control.image_src = card12imglist[0]
        else:
            e.control.image_src = card12imglist[1]
        page.update()

    card12 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card12img,
                         on_click=card12imgfunc)
    
#-------------------------------------------------------------------#
#card 13-------------------------------------------------------------#

    card13imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/hermancard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card13img = card13imglist[0]

    def card13imgfunc(e):
        if e.control.image_src == card13imglist[1]:
            e.control.image_src = card13imglist[0]
        else:
            e.control.image_src = card13imglist[1]
        page.update()

    card13 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card13img,
                         on_click=card13imgfunc)
    
#-------------------------------------------------------------------#
#card 14-------------------------------------------------------------#

    card14imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/joecard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card14img = card14imglist[0]

    def card14imgfunc(e):
        if e.control.image_src == card14imglist[1]:
            e.control.image_src = card14imglist[0]
        else:
            e.control.image_src = card14imglist[1]
        page.update()

    card14 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card14img,
                         on_click=card14imgfunc)
    
#-------------------------------------------------------------------#
#card 15-------------------------------------------------------------#

    card15imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/mariacard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card15img = card15imglist[0]

    def card15imgfunc(e):
        if e.control.image_src == card15imglist[1]:
            e.control.image_src = card15imglist[0]
        else:
            e.control.image_src = card15imglist[1]
        page.update()

    card15 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card15img,
                         on_click=card15imgfunc)
    
#-------------------------------------------------------------------#
#card 16-------------------------------------------------------------#

    card16imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/maxcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card16img = card16imglist[0]

    def card16imgfunc(e):
        if e.control.image_src == card16imglist[1]:
            e.control.image_src = card16imglist[0]
        else:
            e.control.image_src = card16imglist[1]
        page.update()

    card16 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card16img,
                         on_click=card16imgfunc)
    
#-------------------------------------------------------------------#
#card 17-------------------------------------------------------------#

    card17imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/paulcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card17img = card17imglist[0]

    def card17imgfunc(e):
        if e.control.image_src == card17imglist[1]:
            e.control.image_src = card17imglist[0]
        else:
            e.control.image_src = card17imglist[1]
        page.update()

    card17 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card17img,
                         on_click=card17imgfunc)
    
#-------------------------------------------------------------------#
#card 18-------------------------------------------------------------#

    card18imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/petercard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card18img = card18imglist[0]

    def card18imgfunc(e):
        if e.control.image_src == card18imglist[1]:
            e.control.image_src = card18imglist[0]
        else:
            e.control.image_src = card18imglist[1]
        page.update()

    card18 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card18img,
                         on_click=card18imgfunc)
    
#-------------------------------------------------------------------#
#card 19-------------------------------------------------------------#

    card19imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/philipcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card19img = card19imglist[0]

    def card19imgfunc(e):
        if e.control.image_src == card19imglist[1]:
            e.control.image_src = card19imglist[0]
        else:
            e.control.image_src = card19imglist[1]
        page.update()

    card19 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card19img,
                         on_click=card19imgfunc)
    
#-------------------------------------------------------------------#
#card 20-------------------------------------------------------------#

    card20imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/richardcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card20img = card20imglist[0]

    def card20imgfunc(e):
        if e.control.image_src == card20imglist[1]:
            e.control.image_src = card20imglist[0]
        else:
            e.control.image_src = card20imglist[1]
        page.update()

    card20 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card20img,
                         on_click=card20imgfunc)
    
#-------------------------------------------------------------------#
#card 21-------------------------------------------------------------#

    card21imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/robertcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card21img = card21imglist[0]

    def card21imgfunc(e):
        if e.control.image_src == card21imglist[1]:
            e.control.image_src = card21imglist[0]
        else:
            e.control.image_src = card21imglist[1]
        page.update()

    card21 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card21img,
                         on_click=card21imgfunc)

#-------------------------------------------------------------------#
#card 22-------------------------------------------------------------#

    card22imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/samcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card22img = card22imglist[0]

    def card22imgfunc(e):
        if e.control.image_src == card22imglist[1]:
            e.control.image_src = card22imglist[0]
        else:
            e.control.image_src = card22imglist[1]
        page.update()

    card22 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card22img,
                         on_click=card22imgfunc)

#-------------------------------------------------------------------#
#card 23-------------------------------------------------------------#

    card23imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/susancard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card23img = card23imglist[0]

    def card23imgfunc(e):
        if e.control.image_src == card23imglist[1]:
            e.control.image_src = card23imglist[0]
        else:
            e.control.image_src = card23imglist[1]
        page.update()

    card23 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card23img,
                         on_click=card23imgfunc)

#-------------------------------------------------------------------#
#card 24-------------------------------------------------------------#

    card24imglist = ["C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/tomcard.png",
                    "C:/Users/leese/OneDrive/Desktop/coding/Python/Py2/guesswhocards/xbackcard.png"]
    card24img = card24imglist[0]

    def card24imgfunc(e):
        if e.control.image_src == card24imglist[1]:
            e.control.image_src = card24imglist[0]
        else:
            e.control.image_src = card24imglist[1]
        page.update()

    card24 = ft.Container(margin=10,
                        padding=10,
                         height=150,
                         width=100,
                         image_src=card24img,
                         on_click=card24imgfunc)

#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#

    def setblueboard(e):
        page.bgcolor = "#14199c"
        page.update()

    blueboard = ft.ElevatedButton(text="Blue Board", on_click=setblueboard)

    def setredboard(e):
        page.bgcolor = "#9c1414"
        page.update()

    redboard = ft.ElevatedButton(text="Red Board", on_click=setredboard)

#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#

    row1 = ft.Row(controls=[card1,card2,card3,card4,card5,card6,card7,card8])
    row2 = ft.Row(controls=[card9,card10,card11,card12,card13,card14,card15,card16])
    row3 = ft.Row(controls=[card17,card18,card19,card20,card21,card22,card23,card24])
  
    boardcolor = ft.Row(controls=[blueboard,redboard])

    page.add(row1,row2,row3,boardcolor)

ft.app(target = main)