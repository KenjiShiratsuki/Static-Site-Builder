def extract_title(markdown):
    lines = markdown.splitlines(keepends=True)
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            if not title:
                raise ValueError("h1 title has no text")
            return title
    raise ValueError("no h1 title found")