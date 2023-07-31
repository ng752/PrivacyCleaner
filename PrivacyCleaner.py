import os
import random

def overwrite_with_random_data(file_path):
    with open(file_path, 'wb') as file:
        file_size = os.path.getsize(file_path)
        for _ in range(file_size):
            # Zufälliges Byte generieren und schreiben
            random_byte = bytes([random.randint(0, 255)])
            file.write(random_byte)

def format_drive(drive_identifier):
    # Stelle sicher, dass das Laufwerk nicht das aktuelle Laufwerk ist oder das Betriebssystem-Laufwerk!
    if drive_identifier == os.getenv('SystemDrive'):
        print("Das Formatieren des Betriebssystem-Laufwerks ist nicht erlaubt.")
        return

    # Überprüfen, ob die angegebene Festplatte existiert
    if not os.path.exists(drive_identifier):
        print(f"Das Laufwerk '{drive_identifier}' existiert nicht.")
        return

    # Frage die Bestätigung des Benutzers ab, um unerwünschte Datenverluste zu vermeiden
    confirm = input(f"Bist du sicher, dass du das Laufwerk '{drive_identifier}' formatieren möchtest? (ja/nein): ")
    if confirm.lower() != 'ja':
        print("Formatierung abgebrochen.")
        return

    # Schleife über alle Dateien und Verzeichnisse im Laufwerk
    for root, _, files in os.walk(drive_identifier):
        for file in files:
            file_path = os.path.join(root, file)
            overwrite_with_random_data(file_path)

    print(f"Das Laufwerk '{drive_identifier}' wurde erfolgreich formatiert.")

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Verwendung: python format_drive.py <Laufwerkskennung>")
        sys.exit(1)

    drive_to_format = sys.argv[1]
    format_drive(drive_to_format)