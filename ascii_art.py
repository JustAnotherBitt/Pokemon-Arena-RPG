import pyfiglet


def game_name():
    terminal_width = 80

    f = pyfiglet.Figlet(font='standard', width=terminal_width)

    # Divide o texto em duas partes
    part1 = f.renderText('Pokemon').splitlines()  # "Pokemon"
    part2 = f.renderText('Arena RPG').splitlines()  # "Arena RPG"

    # Centraliza cada parte em uma largura de 80
    part1 = '\n'.join([line.center(terminal_width) for line in part1])
    part2 = '\n'.join([line.center(terminal_width) for line in part2])

    # Exibe as partes centralizadas
    print(part1)
    print(part2)
