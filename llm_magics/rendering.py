import html

from IPython.display import HTML, Markdown, display  # type: ignore


def render_response(content: str | None) -> None:
    if content is None:
        display(Markdown("No response from the chat client."))
        return
    blocks = split_markdown_content_between_code_blocks(content)
    for block, block_type in blocks:
        if block_type is None or block_type == "":
            display(Markdown(block))
        else:
            display(HTML(create_code_block(block, block_type)))

    display(HTML(html_header))


def display_markdown(content: str) -> None:
    display(Markdown(content))


def create_code_block(code: str, language: str = "python") -> str:
    # Escape HTML special characters in the code
    escaped_code = html.escape(code)

    html_template = """
    <div class="code-block-container">
        <button class="copy-button" onclick="copyCode(this)">Copy</button>
        <pre><code class="language-{language}">{code}</code></pre>
    </div>
    """
    return html_template.format(language=language, code=escaped_code)


# Include the Highlight.js library and styles once
html_header = """
<!-- Include Highlight.js CSS and JS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/default.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
<script>hljs.highlightAll();</script>

<!-- Include Prism.js CSS and JS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-okaidia.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-java.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-cpp.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-swift.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-markup.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-css.min.js"></script>

<style>
/* Code block container styles */
.code-block-container {{
    position: relative;
    margin: 8px 0;
    font-family: monospace;
}}

pre {{
    margin: 0;
    padding: 8px;
    background-color: #f5f5f5;
    border-radius: 4px;
    overflow: auto;
    font-size: 14px;
    line-height: 1.5;
}}

code {{
    font-family: monospace;
}}

/* Copy button styles */
.copy-button {{
    position: absolute;
    top: 16px;
    right: 16px;
    padding: 2px 6px;
    background-color: transparent;
    color: #007acc;
    border: none;
    cursor: pointer;
    font-size: 12px;
    border-radius: 3px;
    text-decoration: underline;
}}

.copy-button:hover {{
    background-color: rgba(0, 0, 0, 0.05);
}}

.copy-button:focus {{
    outline: none;
}}

</style>

<script>
function copyCode(button) {{
    var code = button.nextElementSibling.innerText;
    navigator.clipboard.writeText(code).then(function() {{
        var originalText = button.innerText;
        button.innerText = 'Copied';
        setTimeout(function() {{
            button.innerText = originalText;
        }}, 2000);
    }});
}}
</script>
"""


def split_markdown_content_between_code_blocks(content: str) -> list[tuple[str, str]]:
    """Searches for ``` code blocks in the content and returns a
    list of code blocks and markdown content.
    The output list will have alternating markdown and code block strings of
    format [(text, "markdown"), (code, "python"), (code, "html") ...]
    """
    code_blocks = []
    lines = content.split("\n")
    block: list[str] = []
    block_type = ""
    for line in lines:
        if line.startswith("```"):
            if block:
                code_blocks.append(("\n".join(block), block_type))
                block = []
            block_type = line[3:].strip()
        else:
            block.append(line)
    if block:
        code_blocks.append(("\n".join(block), block_type))
    return code_blocks
