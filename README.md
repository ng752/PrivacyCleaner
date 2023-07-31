# PrivacyCleaner

PrivacyCleaner ist ein Python-Programm zur sicheren Löschung von Festplatteninhalten, um die Privatsphäre des Vorbesitzers zu schützen, bevor die Festplatte weiterverkauft oder entsorgt wird.

**WICHTIG:** Die Verwendung dieses Programms kann zu einem unwiederbringlichen Datenverlust führen. Stelle sicher, dass du die richtige Festplatte auswählst und dass du alle wichtigen Daten gesichert hast, bevor du das Programm ausführst.

## Funktionalität

PrivacyCleaner bietet folgende Funktionalität:

1. Überschreibt den gesamten Inhalt der ausgewählten Festplatte mit zufälligen Daten, um eine sichere Datenlöschung zu gewährleisten.
2. Schützt das Systemlaufwerk (Laufwerk, auf dem das Betriebssystem installiert ist) vor versehentlichem Löschen.

## Systemanforderungen

- Python 3.x

## Anleitung

1. Stelle sicher, dass Python 3 auf deinem System installiert ist.
2. Clone dieses Repository oder lade die ZIP-Datei herunter und extrahiere sie.
3. Navigiere im Terminal oder der Kommandozeile zum Verzeichnis des PrivacyCleaner-Programms.

4. Führe das Programm aus und gib die Festplattenkennung ein, die du löschen möchtest:

**HINWEIS:** Vergewissere dich, dass du die richtige Festplattenkennung angibst. Die Daten auf der ausgewählten Festplatte werden dauerhaft gelöscht.

Beispiel:

```
python privacy_cleaner.py /dev/sdb
```


5. Bestätige die Aktion, wenn dazu aufgefordert wird.

```
Bist du sicher, dass du das Laufwerk '/dev/sdb' formatieren möchtest? (ja/nein):
```

6. Das Programm wird nun den gesamten Inhalt der ausgewählten Festplatte mit zufälligen Daten überschreiben. Dieser Vorgang kann einige Zeit in Anspruch nehmen, abhängig von der Größe der Festplatte.

7. Sobald der Vorgang abgeschlossen ist, wird eine Erfolgsmeldung angezeigt:

```
Das Laufwerk '/dev/sdb' wurde erfolgreich formatiert.
Die Festplatte ist jetzt sicher gelöscht und kann weiterverkauft oder entsorgt werden.
```

**HINWEIS:** Wenn du dir nicht sicher bist, wie du das Programm verwenden sollst oder welche Festplatte du löschen möchtest, wende dich an einen Fachmann oder verwende professionelle Datenträgerlöschungs-Tools.

## Haftungsausschluss

Die Verwendung dieses Programms erfolgt auf eigene Gefahr. Der Entwickler übernimmt keine Haftung für Datenverluste oder andere Schäden, die durch die Verwendung dieses Programms entstehen.

## Lizenz

Dieses Programm ist unter der MIT-Lizenz lizenziert. Weitere Informationen findest du in der [Lizenzdatei](LICENSE).