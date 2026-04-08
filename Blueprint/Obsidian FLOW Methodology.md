---
min-impact: 4
created-after: 2024-09-01
progress: done
---
# TOC

```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.path.startsWith("Vault")'
    - blueprint.contains(this)
    - impact >= this["min-impact"]
    - formula.Created >= this["created-after"]
views:
  - type: table
    name: "TOC"
    sorts:
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - impact
      - progress
      - formula.Created
```

# Khác

```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.path.startsWith("Vault")'
    - blueprint.contains(this)
    - "!impact"
views:
  - type: table
    name: Others
    order:
      - file.name
      - impact
      - progress
      - formula.Created
    sort:
      - property: impact
        direction: DESC
    sorts:
      - property: rank
        direction: DESC
      - property: formula.Created
        direction: DESC

```

# Hoàn thiện

```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.path.startsWith("Vault")'
    - blueprint.contains(this)
    - impact >= this["min-impact"]
    - progress == "done"
views:
  - type: table
    name: "Done"
    sorts:
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - impact
      - progress
      - formula.Created
```