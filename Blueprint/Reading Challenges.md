---
min-impact: 4
created-after: 2024-09-18
genre:
  - Business & Economics
  - Self-Help
  - Psychology
  - Family & Relationships
  - Religion & Spirituality
progress: archived
---

```base
formulas:
  Title: 'file.asLink("![](" + cover + ")")'
  Author: 'list(author).join(", ")'
  Genre: 'list(category).join(" & ")'
filters:
  and:
    - file.path.startsWith("Vault/bookshelf")
    - or:
        - blueprint == link("Reading Challenges")
        - tags.contains("book")
    - this["genre"].contains(category)
views:
  - type: table
    name: "Overview"
    sorts:
      - property: category
      - property: rating
        direction: DESC
      - property: avg_rating
        direction: DESC
    order:
      - formula.Title
      - formula.Author
      - formula.Genre
      - summary
```
