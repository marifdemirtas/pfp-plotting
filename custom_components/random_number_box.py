from docutils import nodes
from docutils.parsers.rst import Directive

# @register_tag('randomnumberbox')
class RandomNumberBox(Directive):
    has_content = False

    def run(self):
        html = """
        <div id="random-number-box" style="border: 1px solid #000; padding: 10px; width: 200px; text-align: center;">
            <p id="random-number">Click the button to generate a random number</p>
            <button id="random-number-button">Generate Number</button>
        </div>
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('random-number-button').addEventListener('click', function() {
                var randomNumber = Math.floor(Math.random() * 10) + 1;
                document.getElementById('random-number').innerText = randomNumber;
            });
        });
        </script>
        """
        return [nodes.raw('', html, format='html')]