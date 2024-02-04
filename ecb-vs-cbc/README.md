# ECB vs CBC

This demo encrypts several images, first using AES in ECB mode and then AES in CBC. The input files are PNG.

## Execution

```bash
# You'll need to have python 3.10 or greater installed.

# Install the dependencies
pip install -r ../requirements.txt

# Run the program
python ./encrypt.py

# And here are the files
007.png
007-aes-cbc.png
007-aes-cbc.png

smu.png
smu-aes-cbc.png
smu-aes-cbc.png

tux.png
tux-aes-cbc.png
tux-aes-cbc.png
```
