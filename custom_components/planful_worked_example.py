
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

        with open('./_sources/_static/new/plans.json') as f:
            data = json.load(f)

        language = self.options.get('language', 'python3')
        autograde = self.options.get('autograde', 'none')

        combined_code = ""
        
        # Combine the contents of all files
        for i, plan in enumerate(sorted(data, key=lambda x: (x['group'], x['order'], x['plan_name']))):
            combined_code += "\n".join(plan['code_template']['lines'])
            for changeable_area, values in plan['code_template'].get('changeable_areas', {}).items():
                random_value = values[0]
                combined_code = combined_code.replace(f"$${changeable_area}$$", f"{random_value}")


        self.options["initialcode"] = combined_code
        self.options["language"] = language


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
