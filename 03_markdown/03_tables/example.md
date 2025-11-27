# Markdown — Tables

## Basic table

| Name  | Age | Role       |
|-------|-----|------------|
| Alice | 24  | Developer  |
| Mark  | 31  | Analyst    |
| John  | 28  | Designer   |

---

## Alignment

### Left aligned (default):

| Column | Value |
|--------|-------|
| A | left |
| B | left |

### Center aligned:

| Column | Value  |
|:------:|:------:|
|   A    | center |
|   B    | center |

### Right aligned:

| Column | Value |
|-------:|------:|
|      A | right |
|      B | right |

## Complex table (PBEP-style)

| Step | Action          | Description               |
|------|-----------------|---------------------------|
| 1    | Create files    | Initialize task structure |
| 2    | Edit example.md | Add Markdown tables       |
| 3    | Write README.md | Describe the task         |
| 4    | Commit          | Save changes to git       |

## Notes
- Tables require a header separator row (`---`)
- Columns are separated by pipes (`|`)
- Alignment is controlled with colons (`:`)