# test-openai-imagegen


ensure you have python installed:
`which python`

if you don't have python, install homebrew first: 
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

then install python:
`brew install python`

create a virtualenv:
`python -m venv venv`

then activate it:
`source venv/bin/activate`

check you're in the right venv by running
`which python`

it should return something like: 
`/Users/sarahpak/repos/test-openai-imagegen/venv/bin/python`


## packages
install openai package
`pip install --upgrade openai`

then pip install dotenv
`pip install python-dotenv requests Pillow`


# to run
`python generate_images.py`
