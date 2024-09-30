---
min-impact: 4
created-after: 2024-08-01
---

```dataview
TABLE impact, created
FROM -"6. Vault"
WHERE contains(string(join(blueprint, "  ")), this.file.name) AND number(impact) >= number(this.min-impact) AND date(created, "yyyy-MM-dd HH:mm:ss") >= date(this.created-after)
SORT rank DESC, created DESC
```


## Others

```dataview
TABLE impact, created
FROM -"6. Vault"
WHERE contains(string(join(blueprint, "  ")), this.file.name) AND none(list(impact))
SORT rank DESC, created DESC
```
