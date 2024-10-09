from pathlib import Path
import shutil

# ANSI escape codes for colored output
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"

def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
    if path.is_dir():
        print(indent + prefix + COLOR_BLUE + str(path.name) + COLOR_RESET)
        indent += "    " if prefix else ""

        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))

def copy_files(source_dir, destination_dir):
    destination_dir.mkdir(parents=True, exist_ok=True)

    for source_file in source_dir.rglob("*"):
        if source_file.is_file():
            shutil.copy2(source_file, destination_dir)

if __name__ == "__main__":
    root = Path(input("Введіть шлях до директорії: "))
    display_tree(root)

    destination_name = input("Введіть назву нової директорії для копіювання файлів: ")
    destination_dir = Path(destination_name)

    try:
        copy_files(root, destination_dir)
        print("Файли успішно скопійовані.")
    except Exception as e:
        print(f"Упс, щось пішло не так: {str(e)}")