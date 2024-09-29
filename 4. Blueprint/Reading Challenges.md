---
min-impact: 4
created-after: 2024-09-18
genre:
  - Business & Economics
  - Self-Help
  - Psychology
  - Family & Relationships
  - Religion & Spirituality
---

```dataview
TABLE WITHOUT ID "![](" + cover + ")" + file.link as Title, join(author, ", ") as Author, join(category, " & ") as Genre, summary as Summary
FROM "6. Vault/bookshelf" 
WHERE blueprint = [[Reading Challenges]] OR contains(tags, "book") 
AND contains(this.genre, category) 
SORT category, rating, avg_rating desc
```
