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

```base
formulas:
  Created: 'if(created, created, file.ctime)'
filters:
  and:
    - '!file.inFolder("Vault")'
    - file.ctime.date() == date(this["created"]).date()
properties:
  impact:
    displayName: Impact
  formula.Created:
    displayName: Created
views:
  - type: table
    name: "Daily Notes"
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