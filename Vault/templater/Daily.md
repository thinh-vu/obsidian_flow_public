---
aliases: 
tags: 
created: 2026-03-28 22:36:18
feeling: 
summary:
---
## Missions ✨


## Thoughts 💬


## Notes 📝

```dataview
TABLE impact as Impact, created as Created
FROM -"6. Vault"
WHERE dateformat(file.ctime,"yyyy-MM-dd") = dateformat(date(this.created, "yyyy-MM-dd HH:mm:ss"), "yyyy-MM-dd")
SORT rank DESC, created DESC
```