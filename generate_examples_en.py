import json  # loads image list from manifest.json

# Open the manifest file and read image data
with open("manifest.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create a new markdown file for the English gallery
with open("examples-en.md", "w", encoding="utf-8") as f:
    f.write("# 📸 Image Gallery\n\n")

    # For each image, write its data to the markdown file
    for image in data:
        f.write(f"## ![{image['title_en']}]({image['file']})\n")
        f.write(f"**{image['title_en']}**  \n")
        f.write(f"📅 {image['date']}  \n")
        f.write(f"🏷️ Tags: {', '.join(image['tags'])}  \n")
        f.write(f"📝 {image['description_en']}  \n")
        f.write("\n---\n\n")
