from docutils import nodes
from docutils.parsers.rst import Directive, directives
from random import choice
import re, os

class RandomFillInTheBlankDirective(Directive):
    # Use directives.unchanged to accept strings with spaces
    required_arguments = 1

    def run(self):
        # Allow filenames with spaces by removing quotes if present
        plan_name = self.arguments[0].split('_')[0]
        try:
            file_path = os.path.join('_sources/_static/new', 'plans.json')
            with open(file_path) as f:
                data = json.load(f)

        content = ""
        for d in data:
            if d['plan_name'] == plan_name:
                data = d
                break
        else:
            print("error")
            data = data[0]

        code_template = data['code_template']
        code_lines = code_template['lines']
        changeable_areas = code_template.get('changeable_areas', {})
        for line_data in code_lines:
            content += line_data + "\n"

        # Find all fill-in-the-blank markers (e.g., '____')
        blanks = [(m.start(), m.group()) for m in re.finditer(r'\$\$(.*?)\$\$', content)]
        if not blanks:
            return [nodes.error(None, nodes.paragraph(text="No blank spaces found in the provided content."))]

        # Randomly choose one blank to leave empty
        # Randomly choose one blank to leave empty
        chosen_blank_index, chosen_blank = choice(blanks)
        modified_content = ""
        last_index = 0

        # Replace all blanks with user input but leave the chosen one blank
        for blank_index, blank_text in blanks:
            if blank_index == chosen_blank_index:
                modified_content += content[last_index:blank_index] + '{{ response }}'
            else:
                modified_content += content[last_index:blank_index] + '{{ fill_in }}'
            last_index = blank_index + len(blank_text)

        # Append any remaining content after the last blank
        modified_content += content[last_index:]

        # Create a node for the directive
        node = nodes.literal_block(text=modified_content, language='text')
        return [node]

def setup(app):
    app.add_directive('random_fillintheblank', RandomFillInTheBlankDirective)