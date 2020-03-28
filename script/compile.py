import utils
import os


def main(version=1):
    print(f'[Compiling] Version {version}')

    # Read Previous JSON
    json_path = utils.getJSONPath(version)
    book = utils.loadJSONFrom(json_path)
    print(f'[Found] {len(book.keys())} entries')

    to_be_removed = []
    # Check Previous Entries
    for md5, fileName in book.items():
        current_md5 = utils.getHash(version, fileName)
        if current_md5 != md5:
            utils.colorPrint('RED', f'[DEL] {fileName} -> {md5}')
            to_be_removed.append(md5)

    # Remove obsolete entries
    for md5 in to_be_removed:
        del book[md5]

    # Detect Changes
    FOLDER_PATH = utils.getFolderPath(version)
    for fileName in sorted(os.listdir(FOLDER_PATH)):
        md5 = utils.getHash(version, fileName)

        if md5 in book:
            print(f'[Old] {fileName} -> {md5}')
        else:
            # New Entry
            utils.colorPrint('GREEN', f'[New] {fileName} -> {md5}')
            book[md5] = fileName

    # Save to JSON
    utils.saveJSON(book, json_path)


# Trigger
if __name__ == '__main__':
    main(1)
