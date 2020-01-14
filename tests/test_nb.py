import subprocess
import tempfile
import os

d = "solutions_do_not_open"

def _exec_notebook(fname):
    path = os.path.join(d, fname)
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)



def test_01():
    _exec_notebook("Lab_01_ML Jupyter Pandas review_solution.ipynb")

def test_02():
    _exec_notebook("Lab_02_ML Data Exploration_solution.ipynb")

def test_03():
    _exec_notebook("Lab_03_ML Regression_solution.ipynb")

def test_04():
    _exec_notebook("Lab_04_ML Classification_solution.ipynb")

def test_05():
    _exec_notebook("Lab_05_ML Clustering_solution.ipynb")
