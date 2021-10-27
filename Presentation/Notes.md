# BA Vortrag Notes


## Willkommen zu meinem Vortrag
 * Analyse und Verbesserung von DevEnvironments
 * Unter zu Hilfe name von Tools aus DevOps und Server Welt
 * In Kooperation mit Symbic
 * Überblick Aufbau

## Contents table
Was wird behandelt?

## Goal
 * Verbesserung der Effizienz beim Programmieren:
   * Identifizieren von Aufgaben die redundant/langsam/fehleranfällig sind
   * Konzept entwickeln un diese zu lösen
   * Anwenden des Konzepts auf reales Project at Symbic
   * Evaluieren

## Potential Bottlenecks
 * Neben dem Programmieren auch viele weitere Aufgaben (ohne Wert)
 * Bei Symbic angefangen - initiales setup aufwendig
 * Lokale Testmöglichkeiten eingeschränkt - insbesondere bei Microservices
 * Pflegen von config und Dependencies
 * Probleme durch Unterschiede zwischen Local und Production
 * Activstate Studie **62%** der Entwickler coden weniger als 4h

## Initial Setup
 * Neuer Rechner: IDE, Mail, Language Runtime installieren
 * Projekte Herunterladen und einreichten
 * Selbe Studie: **69%** 1-4 Mal im Jahr - 2-4h
 * 1/5 sogar bis zu 18h
 * GitHub Story: Script (Allein 45min DB migrations)
 * Am Ende das: Etwas vergesses, etwas Fehlt


## Config
 * Maintenance/Testing am meisten Zeit nach (meetings/software design)
 * Incompatieble Programm versionen
 * Production anders als Development - (Linx vs Win)
 * **45%** Windows dev vs. **78%** WebServers
 * Setzen von Konfigurationen zwischen Apps - Kann schnell kompliziert werden
 * Sehr aufwendig besnders bei Microservices - Siehe Netflix

## Lösung
 * Nutzen von Tools aus Server Welt
 * Die zugrundeliegende Hardware und OS abstrakhieren
 * Standartiesierte, konfigiuration aller Anwendungen
 * Diese automatisch erstelleb
 * Damit Testmöglichkeiten zwischen Anwendungen schaffen

## Realisierung
 * Container: Isoliere Runtime für Prozesse OS independent
 * Alle Abhängigkeiten vorhanden
 * Verbraucht weniger Ressourcen als eine VM
 * Einsatz von Docker (gibt auch Podman LXC)

## Welche Probleme gelöst
 * Docker unabhängig vom Host
 * Wird auch in der Produktion viel eingesetzt
 * Alle nötige in einem Container vorhanden
 * Mehr Software Verfügbar
 * Einzelne Dienste können zusammengeschaltet werden
 * Konfiguration ist YMAL/JSON -> gespeichert/versioniert in GIT

## Arch
Beschreibe Abbildung

## Demo
Konkreter machen durch Demo

## Symbic Arch
 * Größeres Projekt
 * IoT Management - Andere Software
 * Nur Ausschnitt - Real mehr als 20 Dienst

## Compose
 * Umsetzung: Der Archtektur als Code
 * Man definiert deren Status/Config
 * Funktioniert auf jedem Rechner mit Docker
 * Keine witeren Programme notwendig

## Ergebnisse
**Good:**
 * Schnellerer start zum programmieren
 * Größere Auswahl an Software (Vorkonfiguriert)
 * Ähnlicher zwischen Kollegen
 * Ähnlicher zu Produktion
 * Isolierte Umgebung - Keine konflikte/kann weniger kaputt gehen

**Bad:**
 * Docker Wissen notwendig
 * Unter Windows I/O Perfomance low

## Alternatives:
**Basic:**
 * Codespaces und GitPod recht jung
 * Zeigt es ist Lösungsbedarf für diese Probleme da
 * GitHub hat eigenes Team umgestellt

**Pros:Cons**
 * Codespaces & GitPod nur Web/VSCode
 * Externe Dienstleister - Cost/Lizenverträge konfrm?
 * Rechenkapazität kann dynamisch angepasst werde
 * Fokus ligt auf eine Umgebung vs Interaktion von mehreren Anwendungen
 * Lokale Tools können genutzt werden
 * Stückweise ausprbieren - hybrid möglich
 * Volle Kontrolle über die Umgebung und Editor der wahl


## Outlook
 * Großes Potential
 * Einsteiger freundliche umgebungen
 * Programmieren unabhängig vom Gerät
 * Dynamischen anpassen von Ressourcen
 * Produktionsähnlicher
