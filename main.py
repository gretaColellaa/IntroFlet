from time import sleep

import flet as ft


def main(page: ft.Page):
    page.bgcolor = "white"
    # 1) Scrivere del testo. -- OUT
    myText = ft.Text(value="Buongiorno!",
                     color="green", size=30)
    page.controls.append(myText)
    page.update()

    myCounter = ft.Text(value="")
    page.controls.append(myCounter)
    page.update()

    # 2) Creare un campo in cui l'utente
    # può scrivere del testo. -- IN, OUT
    txtIn = ft.TextField(label="Nome",
                         value = "Giuseppe",
                         color="green",
                         disabled=False)
    # page.controls.append(txtIn)
    # page.update()
    page.add(txtIn)  # Equivale a page.controls.append seguito da page.update

    # 3) Creare dei bottoni. Alla pressione
    # di un bottone, eseguo del codice. -- IN
    def handleBtnSaluta(e):
        txtOut.value = f"Ciao {txtIn.value}"
        txtIn.value = ""
        page.update()

    btnSaluta = ft.ElevatedButton(text = "Saluta",
                                  on_click=handleBtnSaluta,
                                  bgcolor="green",
                                  color="white")
    txtOut = ft.Text(value = "Come ti chiami?", color="green")

    row3 = ft.Row(controls=[btnSaluta, txtOut])

    page.add(row3)

    # 4) Creare un menu a tendina. -- IN
    dd = ft.Dropdown(label="Opzioni",
                     hint_text="Seleziona opzione",
                     options=[ft.dropdown.Option("Opzione 1"), ft.dropdown.Option("Opzione 2")])
    for i in range (3, 20):
        dd.options.append(ft.dropdown.Option(f"Opzione {i}"))

    page.add(dd)

    # 5) Visualizzare lunghi elenchi di testo. -- OUT
    def handleAddLV(e):
        if txtIn2.value == "":
            lv.controls.append(ft.Text("Errore. Aggiungi una stringa valida nel campo.",
                                       color="red"))
            page.update()
        else:
            lv.controls.append(ft.Text(txtIn2.value, color="black"))
            page.update()
    txtIn2 = ft.TextField(label= "Stringa input")
    btnIn2 = ft.CupertinoButton(text= "Aggiungi a ListView",
                                on_click=handleAddLV,
                                bgcolor="blue",
                                color="white")

    row5 = ft.Row(controls = [txtIn2, btnIn2],
                  alignment=ft.MainAxisAlignment.CENTER)
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
    page.add(row5, lv)

    for i in range(100):
        myCounter.value = f"Counter: {i}"
        myCounter.color = ft.colors.random_color()
        page.update()
        sleep(1)



ft.app(target=main, view=ft.AppView.FLET_APP)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
