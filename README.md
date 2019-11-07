# Python encryptor
This simple program, which provides you with ability to encrypt
and decrypt texts with Caesar, Vigenere and Vernam ciphers.
# Testing
I use `pytest` framework.
For more details yu can read `tests/README.md`
## Test results
In `test_results_images` directory you can look at plot
of execution time of versus text size.

In `test_results_text` you can see these results in text format.
## Additional files
* `.travis.yml` - CI configuration.
* `pg200.txt` and `sonnets.txt` - for stress testing and measurements.
* `requirements.txt` - project dependencies.
* `vigenere_model.json` and `caesar_model.json` are needed to test hack mode.