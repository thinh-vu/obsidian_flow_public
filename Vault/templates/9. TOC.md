---
aliases: 
created: {{date:YYYY-MM-DD HH:mm:ss}} 
progress: active
tags: 
  - "#system/blueprint"
category: 
summary: 
---
![[Navigation Bar]]

> [!info] Mục tiêu
> (Điền tóm tắt ngắn gọn hoặc mục tiêu của dự án/blueprint này tại đây)

## 📌 Ghi chú nòng cốt (Core Notes)
- 

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
      - formula.Created
```

## 🗂️ Lược đồ tri thức (Knowledge Map)
```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.inFolder("Vault")'
    - file.hasLink(this.file.name)
    - or:
      - progress == "done"
      - progress == "archived"
      - '!note.progress'
views:
  - type: cards
    name: "Completed Knowledge"
    image: note.cover
    imageAspectRatio: 0.8
    sorts:
      - property: impact
        direction: DESC
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - impact
      - summary
```

## 📦 Lưu trữ (Archived)
```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.inFolder("Vault")'
    - file.hasLink(this.file.name)
    - '!note.impact'
views:
  - type: table
    name: "Unclassified / Others"
    sorts:
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - formula.Created
```