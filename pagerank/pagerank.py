import os
import random
from numpy.random import choice
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    damping_probability = round((1 - damping_factor) / (len(corpus)), 5)
    probability_distribution = {key: damping_probability for key in corpus.keys()}
    for item in list(corpus[page]):
        probability_distribution[item] += round(damping_factor / len(corpus[page]), 5)

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    i = 0
    distribution = {keys: 0 for keys in corpus.keys()}
    page = random.choice(list(corpus.keys()))
    while i < n:
        distribution[page] += 1
        transitions = transition_model(corpus, page, damping_factor)
        possible_pages = []
        probabilities = []
        for keys, values in transitions.items():
            possible_pages.append(keys)
            probabilities.append(values)
        page = choice(possible_pages, 1, replace=False, p=probabilities)[0]
        i += 1

    for key in distribution.keys():
        distribution[key] /= n

    return distribution


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    probabilities = {key: 1 / len(corpus) for key in corpus.keys()}
    linking_to = {key: set() for key in corpus.keys()}
    for key in corpus.keys():
        for link in corpus[key]:
            linking_to[link].add(key)
    i = 0
    while i < 10000:
        for page in corpus.keys():
            other_pages = [probabilities[item] / len(corpus[item]) for item in linking_to[page]]
            probabilities[page] = (1 - damping_factor) / len(corpus) + damping_factor * sum(other_pages)
        i += 1

    return probabilities


if __name__ == "__main__":
    main()
