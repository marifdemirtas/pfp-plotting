from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

# Add a directive to create a box that displays a random number

from random import choice
import json, os
import uuid

# @register_tag('plandisplay')
class PlanDisplay(Directive):
    required_arguments = 0  # JSON file path - not in use
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {}
    option_spec.update({
        'plan': directives.unchanged,
    })
    has_content = False

    def run(self):
        file_path = os.path.join('_sources/plans.json')

        with open(file_path) as f:
            data = json.load(f)

        # find the dict in the list 'data' that has 'plan_name' == self.arguments[1]
        for d in data:
            if d['plan_name'] == self.options.get('plan', ''):
                data = d
                break
        else:
            data = data[0]

        name = data['plan_name']
        goal = data['goal']
        code_template = data['code_template']
        
        code_lines = code_template['lines']
        changeable_areas = code_template.get('changeable_areas', {})
        changeable_areas_colors = code_template.get('changeable_areas_colors', {})

        # HTML structure
        html_code = '<div class="plan-display-container">'
        html_code += '<div class="plan-header">'
        # html_code += f'<h3 class="plan-name"></h3>'
        html_code += f'<h5 class="plan-goal">{name}: {goal}</h5>'
        html_code += '</div>'
        html_code += '<div class="code-container">'
        html_code += "<pre>"
        
        # Parse code with highlights and initial randomized values
        for line_data in code_lines:
            html_code += line_data + "\n"
        
        html_code += "</pre></div>"
        
        # Generate a unique ID for this instance
        instance_id = f"plan_display_{uuid.uuid4().hex[:8]}"
        
        # Add annotations section before processing changeable areas
        html_code += f"""
        <div class="annotations-container">
            <button class="annotations-toggle" onclick="toggleAnnotations_{instance_id}(this)">
                <span class="toggle-icon">▶</span> Show What To Write In Changeable Areas
            </button>
            <div class="annotations-content" style="display: none;">
                <div class="annotations-grid">
        """
        
        # Add each annotation
        for placeholder, annotation in reversed(code_template.get('changeable_areas_annotations', {}).items()):
            color = changeable_areas_colors.get(placeholder, '#ffffff')
            html_code += f"""
                    <div class="annotation-item">
                        <span class="annotation-field" style="background-color: {color}">{placeholder}</span>
                        <span class="annotation-description">{annotation}</span>
                    </div>
            """
        
        html_code += """
                </div>
            </div>
        </div>
        """
        
        for placeholder, values in changeable_areas.items():
            # Use placeholder as initial value (template) instead of random example
            # Wrap the template text in a span for highlighting and later updates
            annotation = code_template.get('changeable_areas_annotations', {}).get(placeholder, '')
            html_code = html_code.replace(f"@@{placeholder}@@", f"<span class='changeable template-value {instance_id}' style='background-color: {changeable_areas_colors[placeholder]}' data-original='{placeholder}' title='{annotation}'>{placeholder}</span>")

        # Add the randomize button
        html_code += f"""
        <div class="button-container">
            <button class="plan-button examples-button" onclick="randomizeValues_{instance_id}()">Show Example Values for Template</button>
            <button class="plan-button template-button" onclick="replacePlaceholder_{instance_id}()">Show Template</button>
        </div>
        </div>
        
        <div id="custom-tooltip-{instance_id}" class="custom-tooltip" style="display: none;"></div>
        
        <script>
        // Possible replacements loaded directly from JSON
        const possibleValues_{instance_id} = {json.dumps(changeable_areas)};
        const annotations_{instance_id} = {json.dumps(code_template.get('changeable_areas_annotations', {}))};

        function randomizeValues_{instance_id}() {{
            document.querySelectorAll('.changeable.{instance_id}').forEach((elem) => {{
                const key = elem.getAttribute('data-original');
                const values = possibleValues_{instance_id}[key];
                elem.textContent = values[Math.floor(Math.random() * values.length)];
                elem.classList.add('highlight');
                elem.classList.remove('template-value');
                setTimeout(() => elem.classList.remove('highlight'), 300);
            }});
            
            // Update button states
            document.querySelector('.examples-button').classList.remove('active');
            document.querySelector('.template-button').classList.remove('active');
        }}

        function replacePlaceholder_{instance_id}() {{
            document.querySelectorAll('.changeable.{instance_id}').forEach((elem) => {{
                const key = elem.getAttribute('data-original');
                elem.textContent = key;
                elem.classList.add('highlight');
                elem.classList.add('template-value');
                setTimeout(() => elem.classList.remove('highlight'), 300);
            }});
            
            // Update button states - only template button is active
            document.querySelector('.examples-button').classList.remove('active');
            document.querySelector('.template-button').classList.add('active');
        }}

        function toggleAnnotations_{instance_id}(button) {{
            const content = button.nextElementSibling;
            const icon = button.querySelector('.toggle-icon');
            if (content.style.display === 'none') {{
                content.style.display = 'block';
                icon.textContent = '▼';
                button.classList.add('active');
            }} else {{
                content.style.display = 'none';
                icon.textContent = '▶';
                button.classList.remove('active');
            }}
        }}
        
        // Add event listeners for all changeable elements after the DOM is loaded
        document.addEventListener('DOMContentLoaded', function() {{
            const tooltip = document.getElementById('custom-tooltip-{instance_id}');
            
            // Initialize buttons and changeable elements to show template initially
            document.querySelectorAll('.changeable.{instance_id}').forEach(el => {{
                const key = el.getAttribute('data-original');
                el.textContent = key;  // Show template text
                el.classList.add('template-value');  // Add template styling
            }});
            
            // Initial button state - template button active
            const container = document.getElementById('custom-tooltip-{instance_id}').closest('.plan-display-container');
            if (container) {{
                const examplesButton = container.querySelector('.examples-button');
                const templateButton = container.querySelector('.template-button');
                if (examplesButton) examplesButton.classList.remove('active');
                if (templateButton) templateButton.classList.add('active');
            }}
            
            // Set up tooltip functionality
            document.querySelectorAll('.changeable.{instance_id}').forEach(el => {{
                el.addEventListener('mouseenter', function(e) {{
                    const annotation = this.getAttribute('title');
                    if (annotation) {{
                        this.removeAttribute('title'); // Remove title to prevent native tooltip
                        this.setAttribute('data-tooltip', annotation); // Store it in data attribute
                        
                        tooltip.textContent = annotation;
                        tooltip.style.display = 'block';
                        
                        // Position the tooltip above the element
                        const rect = this.getBoundingClientRect();
                        const tooltipHeight = tooltip.offsetHeight;
                        
                        tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
                        tooltip.style.top = (window.scrollY + rect.top - tooltipHeight - 10) + 'px';
                    }}
                }});
                
                el.addEventListener('mouseleave', function() {{
                    tooltip.style.display = 'none';
                    // Restore title attribute for accessibility
                    const annotation = this.getAttribute('data-tooltip');
                    if (annotation) {{
                        this.setAttribute('title', annotation);
                    }}
                }});
            }});
            
            // Handle scroll events to reposition tooltip
            window.addEventListener('scroll', function() {{
                if (tooltip.style.display === 'block') {{
                    tooltip.style.display = 'none';
                }}
            }});
        }});
        </script>
        """
        
        # Add the CSS only once per page using a global flag
        html_code += """
        <style>
        .plan-display-container {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            padding: 20px;
            font-family: system-ui, -apple-system, sans-serif;
        }

        .plan-header {
            margin-bottom: 20px;
        }

        .plan-name {
            font-size: 24px;
            color: #2c3e50;
            margin: 0 0 10px 0;
            font-weight: 600;
        }

        .plan-goal {
            color: #34495e;
            font-size: 16px;
            line-height: 1.5;
            margin: 0;
        }

        .code-container {
            background: #f8f9fa;
            border-radius: 6px;
            margin: 15px 0;
            overflow: auto;
        }

        .code-container pre {
            margin: 0;
            padding: 15px;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', monospace;
            font-size: 14px;
            line-height: 1.5;
            color: #2c3e50;
        }

        .annotations-container {
            margin: 15px 0;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            overflow: hidden;
        }

        .annotations-toggle {
            width: 100%;
            padding: 10px 15px;
            background: #f8f9fa;
            border: none;
            text-align: left;
            cursor: pointer;
            display: flex;
            align-items: center;
            font-size: 14px;
            color: #2c3e50;
            transition: background-color 0.2s ease;
        }

        .annotations-toggle:hover {
            background: #eaecef;
        }

        .annotations-toggle.active {
            border-bottom: 1px solid #e1e4e8;
        }

        .toggle-icon {
            margin-right: 8px;
            font-size: 12px;
            transition: transform 0.2s ease;
        }

        .annotations-content {
            padding: 15px;
            background: white;
        }

        .annotations-grid {
            display: grid;
            gap: 12px;
        }

        .annotation-item {
            display: grid;
            grid-template-columns: 200px 1fr;
            gap: 12px;
            align-items: center;
        }

        .annotation-field {
            padding: 4px 8px;
            border-radius: 4px;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', monospace;
            font-size: 13px;
        }

        .annotation-description {
            color: #2c3e50;
            font-size: 14px;
            line-height: 1.4;
        }

        .button-container {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        .plan-button {
            color: white !important;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s ease;
        }
        
        .examples-button {
            background-color: #3498db;
        }
        
        .examples-button:hover {
            background-color: #2980b9;
        }
        
        .template-button {
            background-color: #27ae60;
        }
        
        .template-button:hover {
            background-color: #219955;
        }
        
        .plan-button.active {
            box-shadow: 0 0 0 2px white, 0 0 0 4px currentColor;
            font-weight: bold;
            border: 1px solid gray;
        }

        /* Changeable styling */
        .changeable {
            position: relative;
            padding: 2px 4px;
            border-radius: 4px;
            transition: all 0.2s ease;
            cursor: help;
            border-bottom: 1px dotted #666;
        }

        .changeable:hover {
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .changeable.highlight {
            transform: scale(1.1);
        }
        
        .changeable.template-value {
            border: 2px dashed #333;
            padding: 1px 3px; /* Reduce padding to compensate for border */
        }
        
        /* Custom tooltip styling */
        .custom-tooltip {
            position: fixed;
            background: rgba(0,0,0,0.8);
            color: white;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 12px;
            max-width: 300px;
            z-index: 9999;
            pointer-events: none;
            font-family: system-ui, -apple-system, sans-serif;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            transition: opacity 0.2s ease;
            text-align: center;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        
        .custom-tooltip:after {
            content: '';
            position: absolute;
            bottom: -6px;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 0;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-top: 6px solid rgba(0,0,0,0.8);
        }
        </style>
        """
        
        return [nodes.raw('', html_code, format='html')]