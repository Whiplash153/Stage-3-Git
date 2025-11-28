# Markdown

## 1. Basic link
Here is a normal link:
[OpenAI](https://openai.com)

---

## 2. Link with title
Hovering shows a tooltip:
[GitHub](https://github.com "GitHub Homepage")

---
## 3. Reference-style links
Reference links make long documents cleaner:

This is a link to [Python][python-docs] documentation.

[python-docs]: https://docs.python.org/3/

---
## 4. Internal anchors (jumping inside the same file)

Jump to section: [Go to bottom](#bottom-section)

Scroll down here

...

...

...

## Bottom section
<a id="bottom-section"></a>

You jumped to the bottom section

---

## 5. Links to local files
You can link to files inside your repository:

- [task.py](task.py)
- [README.md](README.md)
- [Example from previous task](../04_images/example.md)

These work on GitHub as well.

---

## 6. Email links
Email-style link:
[Contact me](mailto:test@example.com)

---

## 7. Download-style links (raw)
Useful when linking raw files from GitHub:

`https://raw.githubusercontent.com/<username>/<repo>/main/path/to/file`

(You’ll use this later when referencing scripts.)