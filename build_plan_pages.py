'''
Create copies of ./templates/plan_template.rst under ./_sources with the following structure:

From ./_sources/_static/_new/plans.json:
Enumerate each plan starting with group, then order, and then name if their groups and orders are the same
Create a page for each plan in the JSON file, with the following structure:

Naming: plan_{group}_{order}_{plan_name}.rst
In the copied file, replace:
{plan_name} with the plan_name from the JSON file, spaces removed
{plan_id} with the Plan{your_enumeration} (e.g. Plan1)
{plan_metadata_description} with plan['metadata']['description']
{plan_metadata_usage} with plan['metadata']['usage']

'''

from pathlib import Path
import json, re
from shutil import copyfile

with open('./_sources/_static/new/plans.json') as f:
    data = json.load(f)

for i, plan in enumerate(sorted(data, key=lambda x: (x['group'], x['order'], x['plan_name']))):
    group = plan['group']
    order = plan['order']
    name = plan['plan_name']
    plan_id = f"Plan{i + 1}"
    plan_name = name.replace(" ", "")
    plan_metadata_description = plan['plan_metadata']['description']
    plan_metadata_usage = plan['plan_metadata']['usage']

    # Copy the template
    source = Path('./templates/plan_template.rst')
    destination = Path(f'./_sources/plan_{group}_{order}_{plan_name}.rst')
    copyfile(source, destination)

    # Replace the placeholders
    with open(destination, 'r') as f:
        content = f.read()

    content = content.replace("{plan_name}", name)
    content = content.replace("{plan_id}", plan_id)
    content = content.replace("{plan_metadata_description}", plan_metadata_description)
    content = content.replace("{plan_metadata_usage}", plan_metadata_usage)


    ### Replace {plan_code_click} with the code template lines concatenated
    clickable_code = ""
    for line_data in plan['code_template']['lines']:
        if line_data == "":
            continue
        line_data = f"    :click-incorrect:{line_data}:endclick:"
        if '$$' in line_data:
            # replace $$...$$ with __...__ using regex
            line_data = re.sub(r'\$\$(.*?)\$\$', r':endclick: :click-correct:\1:endclick: :click-incorrect:', line_data)
        clickable_code += line_data.replace('\t', '    ') + "\n"

    content = content.replace("{plan_code_click}", clickable_code)

    ### Replace {plan_code_fill} with the code template lines concatenated
    fillable_code = "Fill in the plan to...\n"
    for line_data in plan['code_template']['lines']:
        if line_data == "":
            fillable_code += "\n"
        if '$$' not in line_data:
            fillable_code += f"    ``{line_data}``" + "\n"
        else:
            splitted_line = line_data.split('$$')
            # for i in range(1, len(splitted_line), 2):
            #     fillable_code += f"``{splitted_line[i]}``" + "|blank|" + "\n"
            fillable_code += f"    ``{splitted_line[0]}``" + "|blank|" + "\n"
            answers = plan['code_template']['changeable_areas'][splitted_line[1]]

    fillable_code += "\n"
    for ans in answers:
        if ans == answers[0]:
            fillable_code += "   -    :{answer}: Correct.\n".format(answer=ans)
        else:
            fillable_code += "        :{answer}: Correct.\n".format(answer=ans)
    fillable_code += "        :.*: Incorrect.\n"

    content = content.replace("{plan_code_fill}", fillable_code)

    # Replace {plan_code_fill} with the code template lines concatenated

    with open(destination, 'w') as f:
        f.write(content)

    print(f"Created: {destination}")

print("Done")

