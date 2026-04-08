---
min-impact: 4
created-after: 2024-08-01
progress: medium
---

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
      - property: rank
        direction: DESC
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - impact
      - formula.Created
```


## Others

```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.path.startsWith("Vault")'
    - blueprint.contains(this)
    - '!impact'
views:
  - type: table
    name: "Others"
    sorts:
      - property: rank
        direction: DESC
      - property: formula.Created
        direction: DESC
    order:
      - file.name
      - impact
      - formula.Created
```
