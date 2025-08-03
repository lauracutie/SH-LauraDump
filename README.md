# lauradump.py
A simple python script that decrypts the .rpgmvp files from **[Satisfy Him](https://subscribestar.adult/satisfyhim)** by **OnEdge**.

## Installation
To download this script, use the `git clone` command or simply download the raw `lauradump.py` file. Make sure you have [Python 3](https://www.python.org/downloads) installed.

## Usage
Simply run the `lauradump.py` script from the command line interface and specify the path to the game files as a parameter.

Example:
```sh
python lauradump.py /Users/Laura/Downloads/SatisfyHim
```

If any .rpgmvp files are found in the specified game directory, they will be decoded into base PNG images and put into a new folder named `files` in the same directory from which this script was run. If you want to replicate the folder structure, use the `-f` option.

## Options
To view the available options, run the script with the `-h` or `--help` parameter, or refer to the table below:
|Option|Description|
|------|-----------|
|`-h`, `--help`|Shows the help page and all supported parameters.|
|`-f`, `--folders`|Replicates the folder structure in the `img` directory.|
|`-v`, `--verbose`|Shows detailed logs when running the script.|

## Support
> [!NOTE]
> You can message me on the official **Satisfy Him [Discord Server](https://discord.com/invite/UydmwTXwed)**. My Discord User ID: `1372647007382016187`.

If you are having unexpected results or issues, please open a Issue and I will get back to you. If you'd like to contribute, please propose a Pull Request.

## License
The contents of this repository are licensed under the **MIT** license.