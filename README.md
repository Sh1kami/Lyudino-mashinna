# Людино-машинна взаємодія

Панчишкін Богдан Олександрович · **3ПРс/3** · **варіант 19**.

Навчальні UX-матеріали, wireframes, hi-fi прототипи та перевірки доступності.

| Робота | Тема |
|---|---|
| [ЛР1](Лаб%2001) | Евристики Нільсена: Prometheus на desktop і mobile |
| [ЛР2](Лаб%2002) | User Persona та Empathy Map: академічний обмін |
| [ЛР3](Лаб%2003) | User Journey Map і Site Map: міський транспорт |
| [ЛР4](Лаб%2004) | Wireframes: вивчення іноземних мов |
| [ЛР5](Лаб%2005) | Hi-fi і дизайн-система: медичні нагадування |
| [ЛР6](Лаб%2006) | Самооцінка прототипу за евристиками |
| [ЛР7](Лаб%2007) | План usability-тестування, SUS та TCR |
| [ЛР8](Лаб%2008) | WCAG-аудит і редизайн двох екранів |

## Демонстрація

[MedTime](https://sh1kami.github.io/Lyudino-mashinna/?screen=today) · [Lingua wireframes](https://sh1kami.github.io/Lyudino-mashinna/?app=language&screen=language)

`?version=v1` відкриває вихідну навчальну версію для порівняння доступності. Усі записи демонстраційні, зберігаються лише у браузері; справжні дані про здоров’я вводити не потрібно. Серверних акаунтів і push-сповіщень немає.

## Локальний запуск

```sh
python -m http.server 8091 --directory docs
python Проєкт/scripts/metrics_test.py
```

Звіти в папках лабораторних збережено у форматі PDF. Вихідні файли доступні без архівів.

Анкету та сценарії для ЛР2 і ЛР7 підготовлено для збору реальних відповідей. Дослідницькі гіпотези відділено від спостережень; результати учасників не вигадуються.

## Figma

- [Wireframes Lingua](https://www.figma.com/design/xGhbb5XtmCjM1RbEQ0kkS6/?node-id=3-33) · [інтерактивний прототип](https://www.figma.com/proto/xGhbb5XtmCjM1RbEQ0kkS6/?node-id=3-33&starting-point-node-id=3%3A33)
- [UX-карти: дві UJM та Site Map](https://www.figma.com/design/xGhbb5XtmCjM1RbEQ0kkS6/?node-id=5-247)
- [Hi-fi MedTime](https://www.figma.com/design/i6imKxUP3aBDBRk4e43AbQ/?node-id=1-73) · [інтерактивний прототип](https://www.figma.com/proto/i6imKxUP3aBDBRk4e43AbQ/?node-id=1-73&starting-point-node-id=1%3A73)
- [П’ять WCAG-порівнянь](https://www.figma.com/design/i6imKxUP3aBDBRk4e43AbQ/?node-id=1-220)

## Перевірки

Lighthouse Accessibility: Today **90 → 100**, Add **83 → 100**. Axe: після змін **0 автоматичних порушень** на обох екранах. WAVE: після змін **0 Errors та 0 Contrast Errors** на обох екранах; чотири попередження Possible heading на Today розглянуто окремо. Проведено огляд у Speech Viewer NVDA 2026.3.1; аудіовимову не перевіряли з беззвучним синтезатором.

У ЛР6 є реєстр на 15 знахідок і Excel-файл із формульними підрахунками та графіком. Для ЛР2 та ЛР7 підготовлено анкети й сценарії збору реальних відповідей; вигаданих учасників та результатів немає.

Вихідна навчальна версія для повторного аудиту: [Today](https://sh1kami.github.io/Lyudino-mashinna/v1-today.html) · [Add](https://sh1kami.github.io/Lyudino-mashinna/v1-add.html). Виправлена: [Today](https://sh1kami.github.io/Lyudino-mashinna/v2-today.html) · [Add](https://sh1kami.github.io/Lyudino-mashinna/v2-add.html).
