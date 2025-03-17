import flet as ft


def main(page: ft.Page):
    #un tasto - per decrementare
    #un TextField per visualizzare il valore
    #un tasto + per incrementare
    page.bgcolor = "white"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def handleAdd(e):
        txtCounter.value += 1
        page.update()

    def handleMinus(e):
        txtCounter.value -= 1
        page.update()

    btnAdd = ft.IconButton(ft.Icons.ADD,
                           on_click=handleAdd,
                           bgcolor="green")
    btnMinus = ft.IconButton(ft.Icons.REMOVE,
                             on_click=handleMinus,
                             bgcolor="green")
    txtCounter = ft.TextField(value = 0,
                              width = 80,
                              color="green", disabled=True)
    row = ft.Row(controls=[btnMinus, txtCounter, btnAdd],
                 alignment=ft.MainAxisAlignment.CENTER)
    page.add(row)



ft.app(target=main)
