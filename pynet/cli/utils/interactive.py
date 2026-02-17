from InquirerPy import inquirer

def select_template(templates: list[str]) -> str:
    return inquirer.select(
        message="Selecciona la plantilla:",
        choices=templates,
        default=templates[0],
        pointer="➤",
    ).execute()
