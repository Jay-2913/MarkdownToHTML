import markdown

markdown_text = "# Heading\n\n**Bold text**"  # Corrected the capitalization to "Bold text"
html_text = markdown.markdown(markdown_text)
print(html_text)
