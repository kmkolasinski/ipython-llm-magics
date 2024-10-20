# LLM Magics for Jupyter Notebooks

![CI](https://github.com/kmkolasinski/ipython-llm-magics/actions/workflows/main.yml/badge.svg)



Interact seamlessly with Large Language Models (LLMs) like OpenAI's GPT models directly from your Jupyter Notebook using IPython magics.

https://pypi.org/project/llm-magics/
```bash
pip install llm-magics
```

![Description of GIF](resources/demo.gif)

## Features

- **Interactive Chat Interface**: Engage in a conversational exchange with LLMs within your notebook cells.
- **Customizable Models**: Switch between different OpenAI chat models (e.g., `gpt-3.5-turbo`, `gpt-4`).
- **Set System Messages**: Define system prompts to guide the behavior of the LLM.
- **Persistent Chat History**: Maintain context across multiple interactions.
- **Rich Rendering**: Receive responses with proper formatting, including syntax-highlighted code blocks.
- **Easy Clearing**: Reset the conversation when needed.

## Installation


### Prerequisites

- Python 3.10 or higher
- Jupyter Notebook or JupyterLab
- An [OpenAI API key](https://platform.openai.com/account/api-keys)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kmkolasinski/ipython-llm-magics
   cd llm-magics
   ```

2. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install the Package**

   ```bash
   pip install .
   ```

## Configuration

### Setting the OpenAI API Key

Before using the magics, ensure your OpenAI API key is accessible to the application.

#### Option 1: Environment Variable

Set the `OPENAI_API_KEY` environment variable in your shell:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

#### Option 2: Within the Notebook

Alternatively, set the API key within your notebook:

```python
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'
```

## Usage

### Loading the Extension

In your Jupyter Notebook, load the `llm_magics` extension:

```python
%load_ext llm_magics
```

### Setting the Model

Specify the OpenAI model you want to use:

```python
%llm_set_model gpt-4o
```

*Available models include `gpt-3.5-turbo`, `gpt-4o`, etc.*

### Setting a System Message (Optional)

Define a system message to guide the assistant's behavior:

```python
%llm_set_system_message "You are a helpful assistant."
```

### Starting a Conversation

Use the `%%llm_chat` cell magic to send a message to the LLM:

```python
%%llm_chat

Write a Python function that generates a random integer between 1 and 100.
```

**Response:**

*The assistant will provide a Python function as per your request.*

### Continuing the Conversation

Maintain context across multiple `%%llm_chat` cells:

```python
%%llm_chat

Now modify the function to generate a random floating-point number between 0 and 1.
```

**Response:**

*The assistant will update the function accordingly.*


### Inserting local variables into the chat
```python
not_sorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
expected_output = sorted(not_sorted_list)
```
```python
%%llm_chat

Write python code to sort the list in the descending order using merge sort algorithm.
So that I can write:
input = $not_sorted_list
assert $expected_output == my_merge_sort(input)
```


### Clearing the Conversation History

Reset the chat history when needed:

```python
%llm_clear
```

## Rendering and Syntax Highlighting

The extension includes rich rendering of the LLM's responses:

- Code blocks are syntax-highlighted using [Prism.js](https://prismjs.com/) and [Highlight.js](https://highlightjs.org/).
- Copy buttons are added to code blocks for convenience.
- Markdown formatting is preserved in the responses.

# History

- **v1.1.0**: Initial release with basic chat functionality and rendering.
