---
min-impact: 3
created-after: 2024-09-01
---
# TOC

```dataview
TABLE impact, status, created
FROM -"6. Vault"
WHERE contains(string(join(blueprint, "  ")), this.file.name) AND number(impact) >= number(this.min-impact) AND date(created, "dd-MM-yyyy HH:mm:ss") >= date(this.created-after)
SORT created DESC
```

# Khác

```dataview
TABLE impact, created
FROM -"6. Vault"
WHERE contains(string(join(blueprint, "  ")), this.file.name) AND none(list(impact))
SORT rank DESC, created DESC
```