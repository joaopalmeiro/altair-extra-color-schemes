# altair-extra-color-schemes

Additional named color schemes for [Altair](https://altair-viz.github.io/) via a custom renderer.

## Color schemes

| Color scheme name | Source                                                                                                | Notes                                    |
| ----------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `"dvs"`           | [Data Visualization Standards (DVS)](https://xdgov.github.io/data-design-standards/components/colors) | "Qualitative Colors" > "Example Palette" |

## Development

> [Poetry](https://python-poetry.org/) (version 1.2.0b3)

- `poetry config virtualenvs.in-project true`
- `poetry install`
- `poetry run jupyter lab`
- `poetry run black demo.ipynb`
- `poetry check`

## Deployment

- `poetry version minor` or `poetry version patch`
- `poetry build`

## Notes

- [djLint](https://djlint.com/):
  - `pipx install djlint`
  - `djlint altair_extra_color_schemes/template.jinja --check`
  - `djlint altair_extra_color_schemes/template.jinja --reformat`
  - `djlint altair_extra_color_schemes/template.jinja --profile=jinja`
