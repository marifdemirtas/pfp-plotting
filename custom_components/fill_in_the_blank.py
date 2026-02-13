from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from runestone.common.runestonedirective import RunestoneIdDirective
import json

class FillInTheBlank(RunestoneIdDirective):
    """
    .. fillintheblank:: unique_id
       :code_template: |
          Multiline code template with blanks marked as @@blank1@@, @@blank2@@, etc.
          Can span multiple lines
          With proper indentation
       :correct: ["answer1", "answer2", ...]  # List of correct answers for each blank
       :feedback: ["feedback1", "feedback2", ...]  # List of feedback messages for each blank
       :placeholder: ["placeholder1", "placeholder2", ...]  # List of placeholders for each blank

       Question text goes here...
    """
    required_arguments = 1  # unique_id
    optional_arguments = 0
    has_content = True
    option_spec = RunestoneIdDirective.option_spec.copy()
    option_spec.update({
        'code_template': directives.unchanged_required,
        'correct': directives.unchanged_required,
        'feedback': directives.unchanged,
        'placeholder': directives.unchanged,
    })

    def run(self):
        # Process options
        unique_id = self.arguments[0]
        code_template = self.options.get('code_template', '').strip()
        
        # Parse JSON arrays from options
        try:
            correct_answers = json.loads(self.options.get('correct', '[]'))
            feedback_messages = json.loads(self.options.get('feedback', '[]'))
            placeholders = json.loads(self.options.get('placeholder', '[]'))
        except json.JSONDecodeError:
            # Fallback to single values if not JSON arrays
            correct_answers = [self.options.get('correct', '')]
            feedback_messages = [self.options.get('feedback', 'Try again')]
            placeholders = [self.options.get('placeholder', 'Type your answer here')]

        # Ensure we have enough feedback and placeholders
        while len(feedback_messages) < len(correct_answers):
            feedback_messages.append('Try again')
        while len(placeholders) < len(correct_answers):
            placeholders.append('Type your answer here')

        # Process content (question text)
        question_text = '\n'.join(self.content)

        # Replace each blank placeholder with an input while preserving whitespace
        code_with_input = code_template
        for i, (answer, placeholder) in enumerate(zip(correct_answers, placeholders), 1):
            input_html = f'<input type="text" class="blank-input" data-blank-id="{i}" placeholder="{placeholder}" data-correct="{answer}"/>'
            code_with_input = code_with_input.replace(f'@@blank{i}@@', input_html)

        # Generate HTML with properly escaped curly braces
        html = f"""
        <div class="fill-in-blank-container" id="{unique_id}">
            <div class="question-text">
                {question_text}
            </div>
            <div class="code-template">
                <pre class="code-display"><code>{code_with_input}</code></pre>
            </div>
            <div class="feedback-container" style="display: none;">
                <div class="feedback-text"></div>
            </div>
            <button class="btn-success btn check-answer-btn">Check Me</button>
        </div>

        <style>
        .fill-in-blank-container {{
            background: color(srgb 0.9387 0.9737 0.999);
            border: 4px solid black;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            padding: 20px;
            font-family: system-ui, -apple-system, sans-serif;
        }}

        .question-text {{
            color: #2c3e50;
            font-size: 16px;
            line-height: 1.5;
            margin-bottom: 15px;
        }}

        .code-template {{
            background: #f8f9fa;
            border-radius: 6px;
            margin: 15px 0;
            padding: 15px;
            overflow: auto;
        }}

        .code-display {{
            margin: 0;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', monospace;
            font-size: 14px;
            line-height: 1.5;
            color: #2c3e50;
            white-space: pre;
        }}

        .code-display code {{
            white-space: pre;
        }}

        .blank-input {{
            display: inline-block;
            padding: 4px 2px;
            margin: 0 2px;
            border: 2px solid #ddd;
            border-radius: 4px;
            font-family: inherit;
            font-size: inherit;
            background: white;
            transition: all 0.2s ease;
            width: 10em;
            vertical-align: middle;
        }}

        .blank-input:focus {{
            outline: none;
            border-color: #3498db;
            box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
        }}

        .blank-input.correct {{
            border-color: #2ecc71;
            background-color: #f0fff4;
            color: black;
        }}

        .blank-input.incorrect {{
            border-color: #e74c3c;
            background-color: #fff5f5;
        }}

        .feedback-container {{
            margin: 10px 0;
            padding: 10px;
            border-radius: 4px;
        }}

        .feedback-container.correct {{
            background-color: #f0fff4;
            border: 1px solid #2ecc71;
            color: #2ecc71;
        }}

        .feedback-container.incorrect {{
            background-color: #fff5f5;
            border: 1px solid #e74c3c;
            color: #e74c3c;
        }}
        </style>

        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const container = document.getElementById('{unique_id}');
            const inputs = container.querySelectorAll('.blank-input');
            const checkBtn = container.querySelector('.check-answer-btn');
            const feedbackContainer = container.querySelector('.feedback-container');
            const feedbackText = container.querySelector('.feedback-text');
            const feedbackMessages = {json.dumps(feedback_messages)};

            function checkAnswers() {{
                let allCorrect = true;
                let feedbacks = [];

                inputs.forEach((input, index) => {{
                    const userAnswer = input.value.trim();
                    const correctAnswer = input.dataset.correct;
                    
                    if (userAnswer === correctAnswer) {{
                        input.classList.remove('incorrect');
                        input.classList.add('correct');
                    }} else {{
                        input.classList.remove('correct');
                        input.classList.add('incorrect');
                        allCorrect = false;
                        feedbacks.push(feedbackMessages[index]);
                    }}
                }});

                feedbackContainer.style.display = 'block';
                if (allCorrect) {{
                    feedbackContainer.classList.remove('incorrect');
                    feedbackContainer.classList.add('correct');
                    feedbackText.textContent = 'All correct!';
                }} else {{
                    feedbackContainer.classList.remove('correct');
                    feedbackContainer.classList.add('incorrect');
                    feedbackText.textContent = feedbacks.join(' & ');
                }}
            }}

            checkBtn.addEventListener('click', checkAnswers);
            inputs.forEach(input => {{
                input.addEventListener('keypress', function(e) {{
                    if (e.key === 'Enter') {{
                        checkAnswers();
                    }}
                }});
            }});
        }});
        </script>
        """

        return [nodes.raw('', html, format='html')] 