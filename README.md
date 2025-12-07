# Search Engine Project (Python)

This project was developed for a university assignment where we had to build a small search engine and test how different data structures affect searching performance. The program loads text from a list of Wikipedia URLs and stores all the words using five different data structures:

- Linked List
- Binary Search Tree
- AVL Tree
- Hash Table
- Trie

After loading the data, the user can choose which data structure to use and then search for any keyword. The program prints all URLs where the word appears and also shows how long the search takes.


## How the Project Works

1. The dataset.txt file contains a list of Wikipedia URLs.
2. The program downloads the page content and extracts the text.
3. Every keyword is indexed with the URLs in which it appears.
4. Depending on the user’s choice, the indexing/searching is done using one of the five data structures.

