## 🎯 TASKS

```dataview
TASK
WHERE !completed
```

## ✨ RECENT

```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - impact >= 4
    - formula.Created >= this["created-after"]
views:
  - type: table
    name: "Recent"
    limit: 20
    sorts:
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - file.ctime
```

## ⏱️ ON THIS DAY

```base
filters:
  and:
    - file.name.contains(today().format("-DD"))
    - '!file.name.contains(today().format("-DD-"))'
    - '!file.name.contains(today().format("YYYY-MM-DD"))'
views:
  - type: table
    name: "On this day"
    order:
      - file.name
```


## 👟 STREAKS

```dataview
CALENDAR file.ctime
LIMIT 5
```