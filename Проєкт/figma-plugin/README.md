# Figma development plugin

У Figma Desktop імпортуйте manifest.json через Plugins → Development → Import plugin from manifest. Запустіть плагін і виберіть лабораторну.

Для збереження експорту запустіть з папки Проєкт: `python scripts/export_receiver.py`. Сервер приймає лише локальні запити на 127.0.0.1:8092 та зберігає JSON у Проєкт/exports. Після роботи зупиніть його Ctrl+C. Побудова макетів не потребує сервера; він потрібний лише кнопці експорту.
