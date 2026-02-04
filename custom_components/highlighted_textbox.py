from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

class HighlightedTextbox(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'title': directives.unchanged,
        'color': directives.unchanged,
        'highlight-color': directives.unchanged,
        'highlight-on-load': directives.flag,
    }
    has_content = True

    def run(self):
        title = self.options.get('title', 'Note')
        color = self.options.get('color', '#f9f9c6')  # Default light yellow
        highlight_color = self.options.get('highlight-color', '#ffeb3b')  # Default bright yellow
        highlight_on_load = 'highlight-on-load' in self.options
        
        # Generate a unique ID for this textbox
        import random
        unique_id = f"highlighted-textbox-{random.randint(1000, 9999)}"
        
        content = '\n'.join(self.content)
        
        html = f"""
        <div class="highlighted-textbox-container">
            <div class="highlighted-textbox" id="{unique_id}" style="background-color: {color};">
                <div class="highlighted-textbox-header">
                    <h4 class="highlighted-textbox-title">{title}</h4>
                </div>
                <div class="highlighted-textbox-content">
                    {content}
                </div>
            </div>
        </div>
        
        <script>
        // Apply highlight animation on load if specified
        document.addEventListener('DOMContentLoaded', function() {{
            var shouldHighlight = {str(highlight_on_load).lower()};
            
            if (shouldHighlight) {{
                var textbox = document.getElementById('{unique_id}');
                textbox.style.backgroundColor = '{highlight_color}';
                setTimeout(function() {{
                    textbox.style.backgroundColor = '{color}';
                }}, 1000);
            }}
        }});
        
        // Make element highlight when clicked
        document.getElementById('{unique_id}').addEventListener('click', function() {{
            this.style.backgroundColor = '{highlight_color}';
            setTimeout(function() {{
                document.getElementById('{unique_id}').style.backgroundColor = '{color}';
            }}, 500);
        }});
        </script>
        
        <style>
        .highlighted-textbox-container {{
            margin: 20px 0;
            font-family: system-ui, -apple-system, sans-serif;
        }}
        
        .highlighted-textbox {{
            border-radius: 8px;
            border: 1px solid #e1e4e8;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            padding: 15px;
            transition: background-color 0.5s ease;
            cursor: pointer;
        }}
        
        .highlighted-textbox:hover {{
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }}
        
        .highlighted-textbox-header {{
            margin-bottom: 10px;
        }}
        
        .highlighted-textbox-title {{
            font-size: 18px;
            color: #2c3e50;
            margin: 0 0 5px 0;
            font-weight: 600;
        }}
        
        .highlighted-textbox-content {{
            color: #34495e;
            font-size: 15px;
            line-height: 1.5;
        }}
        </style>
        """
        
        return [nodes.raw('', html, format='html')] 