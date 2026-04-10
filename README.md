<h1 style="text-align:center;" >
<img style="vertical-align: middle;" alt="Title" src="assets/logo.ico" width="64" height="48" /> Jericho
</h1>

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
![Codacy Badge](https://app.codacy.com/project/badge/Grade/2f8590352c8140ea92d377849f7ea06a)
[![Jericho-CI](https://github.com/NY-Daystar/Jericho/actions/workflows/python.yml/badge.svg?branch=main)](https://github.com/NY-Daystar/Jericho/actions/workflows/python.yml)
![License](https://img.shields.io/github/license/ny-daystar/Jericho)
[![Version](https://img.shields.io/github/tag/NY-Daystar/jericho.svg)](https://github.com/NY-Daystar/Jericho/releases)

[![GitHub Releases](https://img.shields.io/github/downloads/ny-daystar/jericho/total)](https://github.com/ny-daystar/jericho/releases)
[![Total views](https://img.shields.io/sourcegraph/rrc/github.com/NY-Daystar/jericho.svg)](https://sourcegraph.com/github.com/NY-Daystar/jericho)

![GitHub watchers](https://img.shields.io/github/watchers/ny-daystar/Jericho) ![GitHub forks](https://img.shields.io/github/forks/ny-daystar/Jericho) ![GitHub Repo stars](https://img.shields.io/github/stars/ny-daystar/Jericho)

![GitHub repo size](https://img.shields.io/github/repo-size/ny-daystar/Jericho) ![GitHub language count](https://img.shields.io/github/languages/count/ny-daystar/Jericho) ![GitHub top language](https://img.shields.io/github/languages/top/ny-daystar/Jericho)
![GitHub issues](https://img.shields.io/github/issues/ny-daystar/Jericho) ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ny-daystar/Jericho)

# Summary

- [User Guide](#user-guide)
- [Requirements](#requirements)
- [For developers](#for-developers)
    - [Explainations](#explainations)
- [Contact](#contact)
- [Credits](#credits)

## User Guide

![Program](/docs/main.png)

This application is a tool to translate english files to french files

1. Download `Jericho` project from
   [this link](https://github.com/NY-Daystar/Jericho/releases/download/v0.2.0/jericho.exe)

1. Launch `jericho.exe`

1. It gonna ask you the `source` folder containing files to translate (default: data/source) like below  
   ![source](docs/tree-source.png)

1. Then select the `target` folder to save translating (default: data/target)  
   ![dest](docs/tree-result.png)

1. At now the application will translate each of your file into `target` folder

## Requirements

- [Python](https://www.python.org/) >= 3.14 && < 3.15

## For developers

### Setup project

1. You need to create a folder data/source with files to translate like this  
   ![source](docs/tree-source.png)

1. Clone repository

```bash
git clone git@github.com:NY-Daystar/Jericho.git
```

1. Open Jericho project
1. Install dependencies

```bash
poetry install --no-root
```

1. Launch project with

```bash
poetry run .
```

or

```bash
poetry run . --debug
```

You can activate git hooks with this command

```bash
git config --global core.hooksPath .githooks
```

### Explainations

```mermaid
flowchart TD
    A[Get all files from source directory]

    subgraph msg [For each file]
        direction TD
        D["<b>Extract</b> content in string"]
        E["<b>Send</b> content to translator"]
        F["<b>Fetch</b> content translated"]
        G["<b>Save</b> content translated into new file"]
        D-->E
        E-->F
        F-->G
    end

    A-->msg
```

## Contact

- To make a pull request: <https://github.com/NY-Daystar/jericho/pulls>
- To summon an issue: <https://github.com/NY-Daystar/jericho/issues>
- For any specific demand by mail: [luc4snoga@gmail.com](mailto:luc4snoga@gmail.com?subject=[GitHub]%jericho%20Project)

## Credits

Made by Lucas Noga.  
Licensed under GPLv3.
