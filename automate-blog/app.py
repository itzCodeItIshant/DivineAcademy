import os
import re

def create_html_page():
    # Read the HTML template file
    with open("automate-blog/template.html", "r", encoding="utf-8") as file:
        template = file.read()

    # Get user input
    num_paragraphs = int(input("Enter the number of paragraphs: "))
    title = input("Enter the blog title: ")
    introduction = input("Enter the introduction: ")

    index_items = []
    paragraphs = []
    for i in range(num_paragraphs):
        paragraph_title = input(f"Enter title for paragraph {i + 1}: ")
        paragraph_input = input(f"Enter paragraph {i + 1}: ")
        paragraph_lines = paragraph_input.splitlines()
        paragraph = ""
        for line in paragraph_lines:
            paragraph += f"<p>{line}</p>\n"
        index_items.append(f"<li>{paragraph_title}</li>")
        paragraphs.append(f"<h2>{paragraph_title}</h2>\n{paragraph}")

    conclusion = input("Enter the conclusion: ")

    # Replace placeholders in the template with user input
    template = template.replace("<!--title-->", title)
    template = template.replace("<!--intro-->", introduction)
    template = template.replace("<!--index-->", "<ul>" + "\n".join(index_items) + "</ul>")
    template = template.replace("<!--paragraphs-->", "\n".join(paragraphs))
    template = template.replace("<!--conclusion-->", conclusion)

    # Create a clean directory name from the blog title
    clean_title = re.sub(r"[^\w\s-]", "", title)
    clean_title = re.sub(r"^\s+|\s+$", "", clean_title)
    clean_title = re.sub(r"\s+", "_", clean_title)

    # Save the final HTML page inside the 'blog' directory
    output_file_path = os.path.join("blogs", f"{clean_title}.html")
    with open(output_file_path, "w") as file:
        file.write(template)

    print(f"HTML page created successfully! Saved as {output_file_path}")

# Call the function to create the HTML page
create_html_page()
