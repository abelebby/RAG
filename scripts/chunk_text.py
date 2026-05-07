from pathlib import Path
import re

# Load text file
text_path = Path("/Users/abel/Desktop/legal_rag/data/extracted_text/UAE_labor_law_2021.txt")

with open(text_path, "r", encoding="utf-8") as file:
    text = file.read()

# Split by sections
chunks = re.split(r"(Article\s*\(\d+\))", text)

# Combine section titles with content
final_chunks = []

for i in range(1, len(chunks), 2):
    title = chunks[i]
    content = chunks[i + 1]

    chunk = title + "\n" + content
    final_chunks.append(chunk.strip())

# Print chunks
for i, chunk in enumerate(final_chunks[:3]):
    print(f"\n--- CHUNK {i+1} ---\n")
    print(chunk[:500])

print(f"\nTotal chunks: {len(final_chunks)}")


# Save chunks 

import json

output_path = Path("/Users/abel/Desktop/legal_rag/data/chunks/chunks.json")

data = [
    {"id": i, "text": chunk}
    for i, chunk in enumerate(final_chunks)
]

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Chunks saved as JSON.")