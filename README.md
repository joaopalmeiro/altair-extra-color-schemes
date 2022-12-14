# altair-extra-color-schemes

Additional named color schemes for [Altair](https://altair-viz.github.io/) via a custom renderer.

## Quickstart

### Installation

Via [pip](https://pip.pypa.io/):

```bash
pip install altair-extra-color-schemes
```

Via [Pipenv](https://pipenv.pypa.io/):

```bash
pipenv install altair-extra-color-schemes
```

Via [Poetry](https://python-poetry.org/):

```bash
poetry add altair-extra-color-schemes
```

Via [PDM](https://pdm.fming.dev/):

```bash
pdm add altair-extra-color-schemes
```

Via [Pyflow](https://github.com/David-OConnor/pyflow):

```bash
pyflow install altair-extra-color-schemes
```

### Usage

```python
import altair as alt
alt.renderers.enable("extra_color_schemes")
```

You can find some example charts in the [`demo.ipynb` notebook](demo.ipynb).

## Color schemes

| Color scheme name | [Type](https://vega.github.io/vega/docs/schemes/) | Source                                                                                                | Notes                                                          |
| ----------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `"dvs"`           | Categorical                                       | [Data Visualization Standards (DVS)](https://xdgov.github.io/data-design-standards/components/colors) | "Featured Colors" and "Qualitative Colors" > "Example Palette" |

## Development

<!-- > [Poetry](https://python-poetry.org/) (version 1.2.0b3) -->

> [Poetry](https://python-poetry.org/) (version 1.2.0)

Add new color schemes to the `altair_extra_color_schemes/full_template.jinja` file

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
  - `djlint formatter.jinja --reformat --format-css --format-js`
- [Default color schemes](https://vega.github.io/vega-lite/docs/scale.html#scheme)
- [DjHTML](https://github.com/rtts/djhtml):
  - `pipx install djhtml`
  - `djhtml -i formatter.html`
- [curlylint](https://www.curlylint.org/):
  - `pipx install curlylint`
  - `curlylint altair_extra_color_schemes/full_template.jinja`
- [Cloudscape Design System](https://www.figma.com/community/file/1130789169293366599) (Figma file)
- Poetry:
  - [Detection of the currently active Python (experimental)](https://python-poetry.org/blog/announcing-poetry-1.2.0/#detection-of-the-currently-active-python-experimental) documentation
  - [Can't install Pandas on Mac M1](https://github.com/pandas-dev/pandas/issues/40611) issue
- `pip --version`
- [Nullish coalescing operator (??): Short-circuiting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator#short-circuiting)
