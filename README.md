# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/alexfayers/pytest-lf-skip/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                 |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|------------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| src/pytest\_lf\_skip/\_\_init\_\_.py |        6 |        6 |        0 |        0 |      0% |       1-8 |
| src/pytest\_lf\_skip/constants.py    |        9 |        9 |        0 |        0 |      0% |      1-21 |
| src/pytest\_lf\_skip/hooks.py        |       22 |       14 |       10 |        2 |     44% |1-17, 34-39, 46-50 |
| src/pytest\_lf\_skip/lf\_skip.py     |       48 |       10 |       20 |        0 |     85% |1-19, 59-60 |
| src/pytest\_lf\_skip/plugin.py       |       14 |        9 |        2 |        0 |     44% |1-12, 36-37 |
|                            **TOTAL** |   **99** |   **48** |   **32** |    **2** | **60%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/alexfayers/pytest-lf-skip/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/alexfayers/pytest-lf-skip/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/alexfayers/pytest-lf-skip/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/alexfayers/pytest-lf-skip/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexfayers%2Fpytest-lf-skip%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/alexfayers/pytest-lf-skip/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.