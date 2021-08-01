# fake-data

[![maintainer is djfurman](https://img.shields.io/badge/maintainer-djfurman-blueviolet)](https://github.com/djfurman)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-blue?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![license is BSD-3](https://img.shields.io/badge/license-BSD--3-yellow)](https://github.com/MyHealthCo/fake-data/blob/main/LICENSE)

Creates fake but realistic data to test cache functionality for a non-existent health care company.

## Disclaimer

This product generates fake data for a company that does not exist. Any resemblance to a real company is only a coincidence.

## Use Case

Fake data is vital in testing applications at scale. Individualized results and deterministic tests are valuable, but not necessarily an indicator of real world performance.

For example, in testing a cache, repeated GET calls using a small data set will likely yield false confidence in performance as items even read from disk will likely remain in RAM if not cached by the actual application codebase.

To attain a more realistic result, we need realistic but fake information that follows the general patterns of the schema but has no possibility of related to even sanitized real data.

## Usage

1. Run `pipenv run python run.py`

### Setup

1. Clone this repository
1. Run `pipenv sync` to create the virtual environment
1. Run `pre-commit install` to install pre-commit hooks; these will now run with each commit and automatically solve issues you may have with the style guide.

### Installation

1. If you are running a Mac, ensure presence of or install [`brew`](https://brew.sh/) a package manager for your Mac.
1. If you don't have a non-system python install python 3.8; if you are working from a Mac, you can achieve this by running `brew install python@3.8`
1. Make your non-system python a priority in your `$PATH` shell variables (see your shell documentation bash/zsh/fish)
1. Install [`pipenv`](https://pipenv.pypa.io/en/stable/) by running `python -m pip3 install pipenv`
1. Install [`pre-commit`](https://github.com/pre-commit/); again from a Mac, this can be achieved running `brew install pre-commit`

## Contributions

All contributions are welcome. Please open an issue or PR as fit to help enhance this utility.

When contributing, please install the pre-commit plugins and follow the style guide.
