import yaml
import re
import os

my_name = "Fernando Zhapa-Camacho"

# Function to bold your name in the author list
def bold_my_name(authors, my_name):
    # Split the authors by comma
    authors_list = [author.strip() for author in authors.split(',')]
    
    # Bold your name in the list
    authors_list = [
        r"\textbf{" + author + "}" if my_name in author else author 
        for author in authors_list
    ]
    
    return ', '.join(authors_list)

# Function to generate the LaTeX entry
def generate_latex_entry(data, my_name):
    authors_bolded = bold_my_name(data['authors'], my_name)
    date = data['date'].split(' ')[-1]
    
    
    # Format the LaTeX entry
    latex_entry = authors_bolded + ". " + date + ". " + data['title'] + ". " + data['venue'] + "."
    
    return date, latex_entry

def process_subsection(root_dir, subsection_name):
    published_items = []

    for filename in os.listdir(root_dir):
        try:
            if not filename.endswith('.md'):
                continue
            with open(os.path.join(root_dir, filename), 'r') as f:
                content = f.read()
                yaml_content = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL).group(1)
                data = yaml.safe_load(yaml_content)
                year, latex_entry = generate_latex_entry(data, my_name)

                published_items.append((year, latex_entry))
        except:
            print(f"Warning: Issues processing {filename}")
    published_items.sort(reverse=True, key=lambda x: x[0])
    published_items = [item[1] for item in published_items]

    string = "\n\n\\cvsubsection{" + subsection_name + "}"
    string += "\n\n\\begin{cvpubs}"
    string += "\n\n".join(published_items)
    string += "\n\n\\end{cvpubs}"
    return string
    
out_file = "../cv/publications_py.tex"



pub_sections = {"Selected": "_selected_publications",
                "Published": "_publications"}


string = "\\cvsection{Publications}"

for section_name, section_dir in pub_sections.items():
    section_dir = f"../../{section_dir}"
    string += process_subsection(section_dir, section_name)
            
with open(out_file, 'w') as f:
    f.write(string)
