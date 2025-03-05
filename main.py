import hashes_tools as ht
import os

def main():
    # Original hashes files directory
    dir_original_hashes_files = "original_hashes_files"
    # Output directory: Original hashes files that are not matched
    dir_original_hashes_not_matched = "original_hashes_not_mached"
    # List of original hashes files name
    file_list = [f for f in os.listdir(dir_original_hashes_files) if os.path.isfile(os.path.join(dir_original_hashes_files, f))]

    hashes_file = ht.load_hashes("server_hashes.txt")

    for hash_file in file_list:
        original_hashes = ht.load_hashes(os.path.join(dir_original_hashes_files, hash_file))
        original_hashes_not_mached, hashes_file = ht.compare_hashes(original_hashes, hashes_file)
        ht.save_hashes(original_hashes_not_mached, os.path.join(dir_original_hashes_not_matched, hash_file))

    ht.save_hashes(hashes_file, os.path.join(dir_original_hashes_not_matched, "server_hashes_not_mached.txt"))
    return 0

if __name__ == "__main__":
    main()