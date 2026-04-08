---
aliases: 
created: {{date:YYYY-MM-DD HH:mm:ss}} 
progress: active
tags: 
  - blueprint
category: 
summary: 
---

```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.path.startsWith("Vault")'
    - blueprint.contains(this)
    - impact >= 4
views:
  - type: table
    name: "Default"
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
