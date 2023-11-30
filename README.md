# test-openai-imagegen


# prerequisites: 
ensure you have python installed:
`which python`

if you don't have python, install homebrew first: 
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

then install python:
`brew install python`

# setup 
1. create a virtualenv:  
`python -m venv venv`

2. then activate it:  
`source venv/bin/activate`

3. check you're in the right venv by running:   
`which python`

4. it should return something like:   
`/Users/$USER/path/to/test-openai-imagegen/venv/bin/python`


## packages
install openai package
`pip install --upgrade openai`

then pip install dotenv
`pip install python-dotenv requests Pillow`


## troubleshooting
if you see an openssl error like this:
```
 NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
```
run: 
`pip3 uninstall urllib3 && pip3 install 'urllib3<2.0'`
I __think__ this is limited to python3.9 so if this doesn't work for you, try python3.11

# to run
`python generate_images.py`
