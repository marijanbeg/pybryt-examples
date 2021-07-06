IPYNBPATH=examples/*.ipynb
PYREFPATH=examples/pybryt-references/*.py
PYTHON?=python

# Run nbval tests on all notebooks.
# nbval is run in lax mode to ignore any bitmaps, timestamps, etc.
test-nbval:
	$(PYTHON) -m pytest -v --nbval-lax $(IPYNBPATH)

# Run flake8 on all *.py files in the repository.
# Ignored errors:
#   * E501: line too long (82 > 79 characters)
#   * E226: missing whitespace around arithmetic operator
test-flake8:
	$(PYTHON) -m flake8 --ignore E501,E226 --filename=*.py

# Run flake8 on all *.ipynb teaching files in the repository.
# Ignored errors:
#   * E501: line too long (82 > 79 characters)
#   * E226: missing whitespace around arithmetic operator
#   * E402: module level import not at top of file
#   * E226: too many leading '#' for block comment (nbgrader requirement)
#   * E702: multiple statements on one line (semicolon)
#   * F811 redefinition of unused ...
test-flake8-nb:
	$(PYTHON) -m flake8_nb --ignore E501,E226,E402,E266,E702,F811 $(IPYNBPATH)

# Run all tests.
test-all: test-nbval test-flake8 test-flake8-nb

# Run all notebooks inplace.
run-ipynb:
	jupyter nbconvert --execute --inplace $(IPYNBPATH)

# Compile PyBryt references (translate *.py to *.pkl files)
compile-refs: run-ipynb

# Delete *.py PyBryt references
clean-py-refs:
	rm $(PYREFPATH)

# Delete *.py PyBryt references
clean-pkl-refs:
	rm $(PKLREFPATH)

# Delete output from Jupyter notebooks inplace.
clean-output:
	jupyter nbconvert --clear-output --inplace $(IPYNBPATH)