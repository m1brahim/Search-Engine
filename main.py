import time
import re
import os
import sys

from structures.linked_list import LinkedListSearch
from structures.bst import BSTSearch
from structures.avl import AVLSearch
from structures.hashtable import HashTableSearch
from structures.trie import TrieSearch

def format_time_seconds_and_microsec(seconds_float):
    secs = int(seconds_float)
    micros = int((seconds_float - secs) * 1_000_000)
    return f"{secs} seconds and {micros} microseconds"

def load_dataset(dataset_file="wikipedia_texts.txt"):
    if not os.path.exists(dataset_file):
        raise FileNotFoundError(f"Dataset file not found: {dataset_file}")

    words_map = {}
    current_url = None
    urls = []

    with open(dataset_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("=== ") and line.endswith(" ==="):
                current_url = line.replace("=== ", "").replace(" ===", "").strip()
                urls.append(current_url)
                continue

            if not line or not current_url:
                continue

            tokens = line.lower().split()
            for t in tokens:
                word = re.sub(r'[^a-z]', '', t)
                if not word:
                    continue
                if word not in words_map:
                    words_map[word] = []
                found = False
                for idx, (url, cnt) in enumerate(words_map[word]):
                    if url == current_url:
                        words_map[word][idx] = (url, cnt + 1)
                        found = True
                        break
                if not found:
                    words_map[word].append((current_url, 1))

    return urls, words_map

def select_structure(mode):
    if mode == "1":
        return LinkedListSearch()
    elif mode == "2":
        return BSTSearch()
    elif mode == "3":
        return AVLSearch()
    elif mode == "4":
        return HashTableSearch()
    elif mode == "5":
        return TrieSearch()
    else:
        return None

def main():
    print("Select mode:\n"
          "1. Linked List\n"
          "2. Binary Search Tree\n"
          "3. AVL Tree\n"
          "4. Hash Table\n"
          "5. Trie\n")

    mode = input("> ").strip()
    engine = select_structure(mode)
    if engine is None:
        print("Invalid mode selected.")
        return

    print("Loading dataset from text file...")
    start = time.perf_counter()
    try:
        urls, dataset = load_dataset("wikipedia_texts.txt")
    except FileNotFoundError as fe:
        print(fe)
        return
    end = time.perf_counter()

    for word, lst in dataset.items():
        engine.insert(word, lst)

    elapsed = end - start
    print(f"Files loaded successfully. {len(urls)} sections loaded from the file in {format_time_seconds_and_microsec(elapsed)}.\n")

    while True:
        try:
            term = input("Please enter a word to search: ").lower().strip()
        except KeyboardInterrupt:
            print("\nExiting.")
            break

        if term == "":
            continue

        term_norm = re.sub(r'[^a-z]', '', term)
        t1 = time.perf_counter()
        results = engine.search(term_norm)
        t2 = time.perf_counter()

        if not results:
            print("No results found.\n")
            continue

        results = sorted(results, key=lambda x: x[1], reverse=True)
        print(f"\n{len(results)} result(s) found in {format_time_seconds_and_microsec(t2 - t1)}.\n")
        for url, count in results:
            print(f"{url}  (keyword appears {count} times)")
        print()

if __name__ == "__main__":
    main()
