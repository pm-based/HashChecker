import os

def load_hashes(hashes_file_path):
    hashes = {}
    try:
        with open(hashes_file_path, 'r') as f:
            for line in f:
                parts = line.strip().rsplit(' ', 1)
                file_path, file_hash = parts
                file_name = os.path.basename(file_path)

                hashes[file_hash] = {
                    'file_path': file_path,
                    'file_name': file_name
                }

    except FileNotFoundError:
        print(f"Errore: File {hashes_file_path} non trovato.")
    return hashes

def compare_hashes(original_hashes, hashes):
    for hash in list(original_hashes.keys()):
        try:
            file = hashes[hash]
            if original_hashes[hash]['file_name'] == file['file_name']:
                original_hashes.pop(hash)
                hashes.pop(hash)
        except KeyError:
            continue
    return original_hashes, hashes

def save_hashes(hashes, output_file_path):
    """ Save the hashes to a text file."""
    with open(output_file_path, 'w') as f:
        for file_hash, data in hashes.items():
            f.write(f"{data['file_path']} {file_hash}\n")
