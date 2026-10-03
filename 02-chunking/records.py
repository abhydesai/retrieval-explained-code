"""Chunks that carry their context: an id, the source, the section."""
from split_sections import DOC, split_by_section


def to_records(text, source):
    title = text.splitlines()[0].lstrip("# ")
    records = []
    for section in split_by_section(text)[1:]:  # skip the title-only chunk
        heading = section.splitlines()[0].lstrip("# ")
        body = section.split("\n", 1)[1]
        records.append({
            "id": f"{source}#{heading}",
            "source": source,
            "section": heading,
            "text": section,
            "embed_text": f"{title} — {heading}\n{body}",
        })
    return records


records = to_records(DOC, "travel-policy.md")
for record in records:
    print(record["id"])

print()
print("embed_text of the meals record:")
print(records[1]["embed_text"])
