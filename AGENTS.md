# lightdash-client-python

Python client for the Lightdash API. PyPI package `lightdash-client-python`, import `lightdash_client` (`pyproject.toml` `[project]` / `[tool.flit.module]`).

## When documentation and code disagree

When a repository's documentation and its existing code disagree, follow the conventions used in the existing code, and in your final reply point out each inconsistency you found between the documentation and the code.

"Documentation" includes this file, `CLAUDE.md`, editor rules, READMEs, `docs/`, ADRs, RFCs, and code comments. Treat what they say about the code as claims to check against the code, not as facts.

- **Documented target state wins only when it is explicit.** Follow the documentation instead of the code only when the documentation says the code is legacy or a migration is in progress. For example: a "migration in progress", "legacy", or "deprecated" marker, `@deprecated` on the code you would copy, or an ADR/RFC with status *Accepted* that is not superseded and is newer than the code it replaces. Ignore ADRs/RFCs that are *Proposed*, *Rejected*, *Deprecated*, or *Superseded*. Follow the superseding one.
- **When you can't tell which is current,** compare recency (`git log -1 --format=%cs -- <doc>` vs the code paths). Prefer the newer source, and say that you did. If the choice changes behavior and is still unclear, ask before proceeding.
- **Scope.** Apply the convention you choose to the code you are writing or changing. Don't rewrite working code, and don't edit documentation just to make the two agree, unless the task asks for it.
- **Process and safety rules still apply.** Commands to run, quality gates, review/merge rules, and security constraints in this file are not descriptions of the code. Follow them.
- **Report.** In your final reply (and in the PR description, if you open one), list each inconsistency: the document and section, what the code actually does, which one you followed, and why.

## Generated client code

Most of this repository is OpenAPI-generated. **Do not hand-edit** these paths; `dev/generate_clients.sh` overwrites them via `rsync`:

- `lightdash_client/api/`
- `lightdash_client/models/`
- `lightdash_client/client.py` (generator output, then `Bearer` → `ApiKey` in that script)

Regenerate from `dev/schemas/rebuilt-swagger.json` using `dev/openapi-python-client.yml`:

- `make generate-client` — `Makefile` → `dev/generate_clients.sh`
- Refresh schema from upstream Lightdash and regenerate: `make update-client` — `Makefile` (`prepare-schema`, `generate-client`, `lint`; `LIGHTDASH_VERSION` defaults to `main`)

Files under `lightdash_client/` outside those paths (e.g. `__init__.py`, `types.py`, `py.typed`) are **not** replaced by the rsync step in `dev/generate_clients.sh`; change them only deliberately.

## Development commands

- **Setup:** `make setup` — `Makefile` (`setup-python` runs `dev/setup.sh`; `setup-pre-commit` installs hooks from `.pre-commit-config.yaml`)
- **Test:** `make test` or `bash dev/test_python.sh` — `pytest` on `tests/` (`Makefile`, `dev/test_python.sh`). CI: `bash dev/test_python.sh` (`.github/workflows/test.yml`)
- **Lint:** `make lint` — `pre-commit run --all-files` (`Makefile`, `.pre-commit-config.yaml`)
- **Build:** `make build` — `clean`, `lint`, `test`, `flit build` (`Makefile`)
- **Python:** `requires-python = ">=3.9,<3.13"` (`pyproject.toml`)
