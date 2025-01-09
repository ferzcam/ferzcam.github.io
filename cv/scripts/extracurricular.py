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
    institution = data['institution']
    position = data['position']
    start_date = data['start_date']
    end_date = data['end_date']
    
    
    # Format the LaTeX entry
    latex_entry = "\\cvhonor {" + institution + "}{" + position + "}{" + "}{" + str(start_date) + " - " + str(end_date) + "}"
    return end_date, latex_entry

def process_subsection(root_dir):
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
        except Exception as e:
            print(f"Warning: Issues processing {filename}")
            raise e
    published_items.sort(reverse=True, key=lambda x: x[0])
    published_items = [item[1] for item in published_items]

    string = "\n\n\\begin{cvhonors}\n\n"
    string += "\n\n".join(published_items)
    string += "\n\n\\end{cvhonors}"
    return string
    
out_file = "../cv/extracurricular_py.tex"

sections = {"Service and Outreach": "_outreach",
            # "Development", "Peer reviews"
            }

string = "\\cvsection{Outreach and Extracurricular Activities}"

section_dir = f"../../_outreach/"

for section in sections:
    section_dir = f"../../_outreach/"
    string += "\n\n\\cvsubsection{" + section + "}"
    string += process_subsection(section_dir)


string += """

\\cvsubsection{Peer Review}

\\begin{small} \color{black}
Bioinformatics \\\\
Journal of Biomedical Semantics \\\\
PLOS ONE \\\\
International Conference on Neural-Symbolic Learning and Reasoning \\\\
European Conference on Artificial Intelligence \\\\
AAAI Fall Symposium Series \\\\
Neurosymbolic Artificial Intelligence \\\\
\\end{small}

"""
    
with open(out_file, 'w') as f:
    f.write(string)
