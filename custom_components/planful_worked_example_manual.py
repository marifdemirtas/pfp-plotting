
from docutils import nodes
from docutils.parsers.rst import Directive
from runestone import activecode
import os
import json
from runestone.common.runestonedirective import (
    RunestoneIdDirective,
)
from docutils.parsers.rst import directives
from collections import defaultdict

class PlanfulWorkedExample(Directive):
    has_content = False
    required_arguments = 1  # First argument is the ID
    optional_arguments = 0
    option_spec = defaultdict(str)
    option_spec.update({
        'files': directives.unchanged_required,
    })

    def run(self):
        # Get directive options
        self.options["name"] = self.arguments[0].strip()

        unique_id = self.arguments[0]
        print(self.arguments)
        fps = self.options.get('files', "").split(',')
        if fps == []:
            error = self.state_machine.reporter.error(
                f"Files not found.",
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno
            )
            return
        print(fps)
        file_paths = [os.path.join('_sources/_static/new', fp) for fp in fps]

        language = self.options.get('language', 'python')
        autograde = self.options.get('autograde', 'none')

        combined_code = ""
        
        # Combine the contents of all files
        for file_path in file_paths:
            if os.path.exists(file_path):
                with open(file_path) as f:
                    data = json.load(f)[0]
                    combined_code += "\n".join(data['code_template']['lines'])
            else:
                error = self.state_machine.reporter.error(
                    f"File '{file_path}' not found.",
                    nodes.literal_block(self.block_text, self.block_text),
                    line=self.lineno
                )
                return [error]

        self.options["initialcode"] = combined_code
        self.options["language"] = 'python3'


        # # Create activecode block
        # from runestone.activecode import ActivcodeNode
        # return [ActivcodeNode(content=self.options, rawsource=combined_code)]
        # activecode_node = nodes.literal_block(combined_code, combined_code)
        # activecode_node['classes'].append('activecode')
        # activecode_node['data-unique-id'] = unique_id
        # activecode_node['data-language'] = language
        # activecode_node['data-autograde'] = autograde
        # activecode_node['data-component'] = 'activecode'
        
        # print(activecode_node.asdom().toxml())
        # return [activecode_node]

        # Create an HTML-like node to embed the activecode block
        activecode_html = (
            f'<div class="activecode" '
            f'data-component="activecode" '
            f'data-uniqueid="{unique_id}" '
            f'data-language="python3" '
            f'data-autograde="{autograde}">\n'
            f'<textarea style="display:none;">\n{combined_code}</textarea>\n'
            f'</div>'
        )

        raw_node = nodes.raw('', activecode_html, format='html')
        return [raw_node]

        # active_code_instance = activecode.ActivcodeNode(
        #     divid=unique_id,
        #     code=combined_code,
        #     language=language,
        #     # instructions=instructions,
        #     # include_feedback=True  # Optionally include feedback features
        # )

        # # Render the component (returns HTML for embedding)
        # rendered_html = active_code_instance.render()
        # return rendered_html

        # literal_block = nodes.literal_block(combined_code, combined_code)
        # literal_block['language'] = language
        # literal_block['classes'].append('activecode')
        # literal_block['ids'].append(unique_id)

        # return [literal_block]
