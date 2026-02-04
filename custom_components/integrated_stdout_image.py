from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
import uuid


class IntegratedStdoutImage(Directive):
    has_content = False
    option_spec = {
        'source_id': directives.unchanged,  # optional: override source element id
        'mime': directives.unchanged,       # optional: mime type, default image/png
        'title': directives.unchanged,      # optional: header text
    }

    def run(self):
        instance_id = f"stdout_image_{uuid.uuid4().hex[:8]}"
        source_id = self.options.get('source_id', 'integrated_1')
        mime = self.options.get('mime', 'image/png')
        title = self.options.get('title', '')

        html_code = f"""
<div class="stdout-image-container" id="{instance_id}">
  <div class="stdout-image-header" {'style="display:none;"' if not title else ''}>{title}</div>
  <div class="stdout-image-controls">
    <button class="stdout-image-button" id="btn_{instance_id}" type="button">Show Image</button>
  </div>
  <div class="stdout-image-target"></div>
</div>
<script>
function renderStdoutImage_{instance_id}() {{
  try {{
    const srcEl = document.getElementById('{source_id}_stdout');
    const container = document.getElementById('{instance_id}');
    const target = container ? container.querySelector('.stdout-image-target') : null;
    const btn = document.getElementById('btn_{instance_id}');
    if (!srcEl || !target) {{
      return;
    }}
    let fullContent = (srcEl.textContent || srcEl.innerText || '').trim();

    const startTag = '@start_figure@';
    const endTag = '@end_figure@';
    const startIdx = fullContent.indexOf(startTag);
    const endIdx = fullContent.indexOf(endTag);
    
    let b64 = '';
    if (startIdx !== -1 && endIdx !== -1) {{
      b64 = fullContent.substring(startIdx + startTag.length, endIdx).trim();
    }} else {{
      b64 = fullContent;
    }}
    console.log("Length of b64:", b64.length)
    console.log("Length of fullContent:", fullContent.length)

    if (!b64) {{
      target.innerHTML = '<div class="stdout-image-error">No Base64 content found.</div>';
      return;
    }}
    const img = document.createElement('img');
    img.alt = 'Decoded image from stdout';
    img.style.maxWidth = '100%';
    img.style.height = 'auto';
    img.src = 'data:{mime};base64,' + b64;
    target.innerHTML = '';
    target.appendChild(img);
    console.log("Bae3:", b64.length);

  }} catch (e) {{
    const container = document.getElementById('{instance_id}');
    if (container) {{
      const target = container.querySelector('.stdout-image-target');
      if (target) {{
        target.innerHTML = '<div class="stdout-image-error">Failed to render image.</div>';
      }}
    }}
  }}
}}

document.addEventListener('DOMContentLoaded', function() {{
  const btn = document.getElementById('btn_{instance_id}');
  if (btn) {{
    btn.addEventListener('click', renderStdoutImage_{instance_id});
  }}
}});
</script>
<style>
.stdout-image-container {{
  background: #fff;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  margin: 16px 0;
  padding: 12px;
  font-family: system-ui, -apple-system, sans-serif;
}}
.stdout-image-header {{
  font-weight: 600;
  margin-bottom: 8px;
  color: #2c3e50;
}}
.stdout-image-controls {{
  margin-bottom: 8px;
}}
.stdout-image-button {{
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
}}
.stdout-image-button:hover {{
  background-color: #2980b9;
}}
.stdout-image-button.active {{
  background-color: #2ecc71;
}}
.stdout-image-error {{
  color: #c0392b;
  font-size: 14px;
}}
</style>
"""

        return [nodes.raw('', html_code, format='html')]
