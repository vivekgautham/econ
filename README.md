# econ

This repository contains various economic models, data connectors, and utility functions.

## Folder Structure

The `src` directory contains the main source code for this project, organized as follows:

-   `src/econlib`: A Python library containing modules for economic analysis.
    -   `common`: Shared utilities for calculations, geography-related data, performance measurement, and file I/O.
    -   `datasets`: Modules to connect to and retrieve data from external sources like FRED (Federal Reserve Economic Data).
    -   `programs`: Implementations of specific algorithms and economic models.
    -   `statsutils`: Tools for statistical analysis.
-   `src/tools`: Standalone command-line scripts that utilize the `econlib` library for various tasks like data visualization and analysis.
-   `logging.ini`: Configuration file for logging.

## Setup

To set up the development environment, run:

```bash
./create_venv.sh
pip install -r requirements.txt
```

## Running Tests

To run tests, navigate to the `src` directory and run `pytest`:

```bash
cd src
pytest
```
