"""Structure first, size as the budget: a recursive splitter."""
from langchain_text_splitters import RecursiveCharacterTextSplitter

from split_sections import DOC, split_by_section

SEPARATORS = ["\n## ", "\n\n", "\n", " ", ""]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=40,
    separators=SEPARATORS,
)
for i, chunk in enumerate(splitter.split_text(DOC)):
    print(f"--- chunk {i}: {len(chunk)} characters, its headings ---")
    for line in chunk.splitlines():
        if line.startswith("#"):
            print(line)

print()
print("the meals section alone, with a budget of 100:")
small = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    separators=SEPARATORS,
)
meals = split_by_section(DOC)[2]
print([len(piece) for piece in small.split_text(meals)])
