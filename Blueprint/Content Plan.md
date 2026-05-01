---
min-impact: 4
created-after: 2024-08-01
progress: active
---
![[Navigation Bar]]

> [!info] Mục tiêu
> Blueprint quản lý toàn bộ các tuyến nội dung, bài viết và video đang được phát triển.

## 📌 Ghi chú nòng cốt (Core Notes)
- [[Obsidian FLOW Methodology]]: Phương pháp cốt lõi.

## 🎯 Tiến độ thực thi (Action Plan)
```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.inFolder("Vault")'
    - file.hasLink(this.file.name)
    - or:
      - progress == "active"
      - progress == "wip"
      - progress == "medium"
      - progress == "raw"
views:
  - type: table
    name: "Tasks & WIP"
    sorts:
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - progress
      - impact
      - publish
      - formula.Created
```

## 🗂️ Lược đồ tri thức (Knowledge Map)
```base
filters:
  and:
    - '!file.inFolder("Vault")'
    - file.hasLink(this.file.name)
    - or:
        - progress == "done"
        - progress == "archived"
        - "!note.progress"
formulas:
  Created: if(created, created, file.ctime)
views:
  - type: cards
    name: Completed Content
    order:
      - file.name
      - impact
      - summary
    sort:
      - property: cover
        direction: DESC
      - property: publish
        direction: ASC
    image: note.cover
    imageAspectRatio: 0.8
    sorts:
      - property: impact
        direction: DESC
      - property: formula.Created
        direction: DESC

```
