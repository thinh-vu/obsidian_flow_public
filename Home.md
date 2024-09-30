## 🎯 TASKS

```dataview
TASK
WHERE !completed
```

## ✨ RECENT

```dataview
TABLE dateformat(date(file.ctime), "MMM dd") as Date
FROM "/"
WHERE number(impact) >= 4 AND date(created, "yyyy-MM-dd HH:mm:ss") >= date(this.created-after)
SORT created DESC
LIMIT 20
```

## ⏱️ ON THIS DAY

```dataview
TABLE file.name as Date
FROM "/"
WHERE contains(file.name, dateformat(date(today), "-dd")) = true AND contains(file.name, dateformat(date(today), "-dd-")) = false AND contains(file.name, dateformat(date(today), "yyyy-MM-dd")) = false
```


## 👟 STREAKS

```dataview
CALENDAR file.ctime
LIMIT 5
```