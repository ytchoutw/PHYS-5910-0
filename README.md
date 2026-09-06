# Artificial Intelligence for Physical Sciences course website

An editable course-site skeleton built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Preview locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. Edit the Markdown files in `docs/`; the preview reloads automatically.

## Before publishing

When the repository is ready, add its `site_url`, `repo_name`, and `repo_url` to `mkdocs.yml`. Push to GitHub and enable **Settings → Pages → Source → GitHub Actions**. The included workflow publishes every push to `main`.

## Licensing

Unless otherwise noted, original course text, slides, exercises, and other
educational content are licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original software
code is licensed under the [MIT License](LICENSE-CODE). See
[LICENSE-CONTENT.md](LICENSE-CONTENT.md) for scope and attribution details.

Third-party datasets, papers, and software keep their own licences, and the
course materials this one builds on are credited in the Acknowledgements section
of `docs/index.md`.
