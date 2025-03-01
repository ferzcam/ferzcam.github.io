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
        r"\honorpositionstyle{" + author + "}" if my_name in author else author 
        for author in authors_list
    ]
    
    return ', '.join(authors_list)

# Function to generate the LaTeX entry

def generate_latex_entry(data, my_name, used_dates=[]):
    award = data['award']
    institution = data['institution']
    date = data['date']
    
    
    # Format the LaTeX entry
    if date in used_dates:
        latex_entry = "\\cvhonor {" + award + "}{" + institution + "}{" + "}{}"
    else:
        latex_entry = "\\cvhonor {" + award + "}{" + institution + "}{" + "}{" + date + "}"
        used_dates.append(date)
    return date, latex_entry, used_dates

def process_subsection(root_dir):
    published_items = []
    used_dates = []
    for filename in os.listdir(root_dir):
        try:
            if not filename.endswith('.md'):
                continue
            with open(os.path.join(root_dir, filename), 'r') as f:
                content = f.read()
                yaml_content = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL).group(1)
                data = yaml.safe_load(yaml_content)
                year, latex_entry, used_dates = generate_latex_entry(data, my_name, used_dates=used_dates)

                published_items.append((year, latex_entry))
        except:
            print(f"Warning: Issues processing {filename}")
    published_items.sort(reverse=True, key=lambda x: x[0])
    published_items = [item[1] for item in published_items]

    string = "\n\n\\begin{cvhonors}"
    string += "\n\n".join(published_items)
    string += "\n\n\\end{cvhonors}"
    return string
    
out_file = "../cv/honors_py.tex"



string = "\\cvsection{Awards}"

section_dir = f"../../_awards/"
string += process_subsection(section_dir)
            
with open(out_file, 'w') as f:
    f.write(string)
