import ast

def get_class_names_from_script(file_path):
    # Die Python-Datei lesen
    with open(file_path, "r") as file:
        file_content = file.read()

    # Den Inhalt der Datei parsen
    tree = ast.parse(file_content)

    # Alle Klassendefinitionen extrahieren
    class_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

    return class_names

# Beispiel für die Verwendung des Skripts
if __name__ == "__main__":
    file_path = "chapters/chapterk+1.py"  # Pfad zu der Python-Datei
    class_names = get_class_names_from_script(file_path)
    print("Gefundene Klassennamen:", class_names)

    for i in class_names:
        print(i, end=" ")