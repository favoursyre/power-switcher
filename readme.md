# Power Switcher

## Disclaimer

This script is for educational purposes only, I don't endorse or promote it's illegal usage

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Languages](#languages)
4. [Installations](#installations)
5. [Usage](#usage)
6. [Run](#run)

## Overview

This script switches the power of a system

## Features

- It either restarts, shutdown or logoffs a system

## Languages

- Python 3.9.7

## Installations

```shell
git clone https://github.com/favoursyre/power-switcher.git && cd power-switcher
```

## Usage

Instantiating the class

```python
mode = "shutdown"
switch = Control().switch(mode)
```

## Run

```shell
python power.py
```
