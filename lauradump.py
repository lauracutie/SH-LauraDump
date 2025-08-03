from pathlib import Path
from argparse import ArgumentParser

arguments: ArgumentParser = ArgumentParser(prog="lauradump.py", description="Dumps the RPG Maker game image assets from Satisfy Him.", epilog="Author: Laura (Discord ID: 1372647007382016187)")
arguments.add_argument("-f", "--folders", help="replicate the folder structure", action="store_true")
arguments.add_argument("-v", "--verbose", help="shows detailed logs", action="store_true")
arguments.add_argument("path", help="game folder path", type=Path)
verbose: bool = False

def debug(message: str):
    if verbose: print(message)

if __name__ == "__main__":
    parsedArguments = arguments.parse_args()
    verbose = parsedArguments.verbose
    createFolders: bool = parsedArguments.folders
    gamePath: Path = parsedArguments.path

    debug("ℹ️ Script started.\n")

    if not gamePath.exists() or not gamePath.is_dir():
        debug("❌Please provide a valid path to the game directory.\n")
    else:
        imagesPath: Path
        for imagesPath in gamePath.rglob("img"):
            outputDir: Path = Path.cwd() / "files"
            outputDir.mkdir(exist_ok=True)

            filePath: Path
            for filePath in imagesPath.rglob("*.rpgmvp"):
                debug(f"ℹ️ Processing file {filePath.name}:")

                try:
                    with filePath.open("rb") as fileHandle:
                        fileBytes: bytearray = bytearray(fileHandle.read())
                        fileBytes = bytearray(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR") + fileBytes[32:]

                        outputPath: Path = Path(outputDir / (filePath.relative_to(imagesPath) if createFolders else filePath.name))
                        if createFolders: outputPath.parent.mkdir(parents=True,exist_ok=True)
                        with outputPath.with_suffix(".png").open("wb") as outputHandle:
                            outputHandle.write(fileBytes)
                            debug("  ✅File decrypted successfully.\n")
                except:
                    debug("  ❌Failed to decrypt the file.\n")

    debug("ℹ️ Script finished.")