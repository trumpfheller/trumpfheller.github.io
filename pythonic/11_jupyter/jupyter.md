---
title: UCB Python - Jupyter
layout: default
---

```bash
python3 -V
cd Desktop
mkdir venv
cd venv
```

### Now you create the virtual environment

```bash
python3 -m venv .
ls -ltr
```

### Now you activate the virtual environment

```bash
source bin/activate
# then check if anything exists in the venv
python3 -m pip freeze
# nothing happens
```

### install Jupyter

```bash
pip install jupyter
```

### now check if Jupyter appears within the virtual environment

```bash
pip install jupyter
python3 -m pip freeze
# you get a list
```

### then start it

```bash
jupyter notebook
```

- it will start in a new tab in your browser [localhost:888/tree]
- otherise look up in terminal the url
- now you start the new Notebook by going to New with the arrow and select Notebook

---

### install anaconda

- via anaconda.com/donwload
- via terminal 
- Anaconda-Navigator. app in cmd and space

```bash
conda list
# packages in environment at /Users/mike/anaconda3:
```