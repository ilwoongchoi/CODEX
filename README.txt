
    # Codex Website Generator

    This folder contains everything you need to generate your website.

    ## How to Use:

    1. **Add Protocols:**
       - Go to `content/protocols`.
       - You will see folders like `Medicine`, `Physics`, etc.
       - Add your protocol text files inside. Make sure they end in `.md` (Markdown).
       - You can copy paste the text I generated for you into these files.

    2. **Add Narratives:**
       - Go to `content/communication`.
       - Create a new text file for your post (e.g., `2025-12-07-My-Thought.md`).
       - Write your explanation inside.

    3. **Build the Site:**
       - Double click `build_website.py` (You need Python installed).
       - OR run `python build_website.py` in your terminal.
       - A new folder called `public` will appear. This is your finished website.

    4. **Publish:**
       - Go to [Netlify Drop](https://app.netlify.com/drop).
       - Drag and drop the `public` folder onto the page.
       - Your site is now live!
    