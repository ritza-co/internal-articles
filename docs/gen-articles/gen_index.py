import os

def create_markdown_links(directory):
    markdown_files = [f for f in os.listdir(directory) if f.endswith('.md')]
    links = []
    
    for file in markdown_files:
        # Create display name by replacing hyphens with spaces and capitalizing appropriately
        display_name = ' '.join([word.capitalize() for word in file[:-3].split('-')])
        # Create relative link
        link = f"* [{display_name}](./{file})"
        links.append(link)
    
    # Join all the links into a single markdown output
    output = '\n'.join(links)
    return output

# Example usage:
directory_path = '.' # Replace with your directory path
markdown_output = create_markdown_links(directory_path)
print(markdown_output)

