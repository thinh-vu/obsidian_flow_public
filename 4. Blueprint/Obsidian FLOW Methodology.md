---
min-impact: 4
created-after: 2024-09-01
---
# TOC

```dataview
TABLE impact, progress, created
FROM -"6. Vault"
WHERE contains(string(join(blueprint, "  ")), this.file.name) AND number(impact) >= number(this.min-impact) AND date(created, "yyyy-MM-dd HH:mm:ss") >= date(this.created-after)
SORT created DESC
```

# Khác

```dataview
TABLE impact, progress, created
FROM -"6. Vault"
WHERE contains(string(join(blueprint, "  ")), this.file.name) AND none(list(impact))
SORT rank DESC, created DESC
```

# Hoàn thiện

```dataview
TABLE impact, progress, created
FROM -"6. Vault"
WHERE contains(string(join(blueprint, "  ")), this.file.name) AND number(impact) >= number(this.min-impact) AND progress = "done"
SORT created DESC
```