# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## Unreleased

### Added

- Fake patient record generation
  - Support for minor/guardians
  - US Centric Pharmacies
  - Employment minor/
- Dependencies for
  - [`faker`](https://faker.readthedocs.io/en/master/index.html)
  - [`pandas`](https://pandas.pydata.org/)
  - [`pyarrow`](https://arrow.apache.org/docs/python/)
- Contribution Support
  - Add [`pre-commit`](https://github.com/pre-commit/) support to include
    - black style enforcement
    - isort import formatting
    - end of file fixer
    - trailing whitespace
    - yaml fixer
