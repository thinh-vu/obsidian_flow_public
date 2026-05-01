---
min-impact: 4
created-after: 2024-09-01
progress: active
---
![[Navigation Bar]]

> [!info] Mục tiêu
> Trái tim của hệ thống: Bản đồ tư duy và cẩm nang hướng dẫn sử dụng phương pháp FLOW PKM để xây dựng nhà máy tri thức.

## 📌 Ghi chú nòng cốt (Core Notes)
- [[1. Giới thiệu phương pháp FLOW]]: Bài viết nền tảng giải thích FLOW là gì.
- [[Cấu trúc thư mục theo phương pháp FLOW]]: Hướng dẫn cấu trúc thư mục.
- [[FLOW - Nhà Máy Sản Xuất Ý Tưởng & Hành Trình Sáng Tạo]]: Triết lý vận hành.

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
  - type: list
    name: FLOW Documentation
    order:
      - file.name
    image: note.cover
    imageAspectRatio: 0.8
    sorts:
      - property: impact
        direction: DESC
      - property: formula.Created
        direction: DESC

```

## 📦 Lưu trữ (Archived)
```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.inFolder("Vault")'
    - file.hasLink(this.file.name)
    - progress == "archived"
views:
  - type: table
    name: "Archived Notes"
    sorts:
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - formula.Created
```