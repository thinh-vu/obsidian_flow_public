---
min-impact: 4
created-after: 2024-09-18
genre:
  - Business & Economics
  - Self-Help
  - Psychology
  - Family & Relationships
  - Religion & Spirituality
progress: active
tags:
  - type/moc
---
![[Navigation Bar]]

> [!info] Mục tiêu
> Quản lý lộ trình đọc sách, theo dõi tiến độ và lưu trữ các bài tóm tắt, đánh giá sách thuộc những chủ đề quan tâm nhất.

## 📌 Ghi chú nòng cốt

```base
filters:
  and:
    - file.inFolder("Vault/bookshelf")
    - or:
        - blueprint == link("Reading Challenges")
        - file.hasTag("book")
    - this["genre"].contains(category)
formulas:
  Title: file.asLink("![](" + cover + ")")
  Author: list(author).join(", ")
  Genre: list(category).join(" & ")
properties:
  note.aliases:
    displayName: title
views:
  - type: cards
    name: Overview
    order:
      - aliases
      - author
      - formula.Genre
      - summary
    sorts:
      - property: category
      - property: rating
        direction: DESC
      - property: avg_rating
        direction: DESC
    image: note.cover

```
