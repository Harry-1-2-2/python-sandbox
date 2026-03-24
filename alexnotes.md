# Things to know

* Open a terminal to run code
* Ctrl+c to cancel any command thats running
* `echo` will print stuff
* `pwd` will print working directory
* `cd` change directory . `cd ..` to go up a directory
* `dir` list files


In the Python file you can write what you like. To actually run it you need to put `python file.name` into the terminal.

## UV

```bash
uv add pandas
uv remove pandas
uv sync   # reinstall all dependencies, change python version etc
uv init --help   # make a new repository
```


## Git

```bash
git add .   # add everything in your current folder and below
git add ./subfolder/*   # everything in subfolder
git commit -m "this should be a helpful git message"
git push

git restore --staged .   # move from staged to unstaged
git restore .            # remove all unstaged changes
```