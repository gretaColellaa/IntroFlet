import flet as ft


def main(page: ft.Page):

    def handleAdd(e):
        if txtIn.value == "":
            print("Il textfield è vuoto.")
            return #se è vuoto non fa nulla
        newCheckbox = ft.Checkbox(label=txtIn.value)
        txtIn.value = ""
        page.add(newCheckbox)

    txtIn = ft.TextField(label= "Aggiungi un elemento qui!",
                         width = 300, color="green")
    btnAdd = ft.ElevatedButton(text="Add", on_click=handleAdd)
    row1 = ft.Row(controls=[txtIn, btnAdd], #per mettere in riga gli elementi
                  alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)


ft.app(target=main)
