#!/usr/bin/env python3.4

from __future__ import division

import csv
import os

from nltk.util import ngrams
from nltk.tokenize.regexp import WordPunctTokenizer


def rouge(candidate, reference, n=2, verbose=False):
    """This is a basic implementation of ROUGE-N.  It calculates the
    n-gram recall of a candidate summary against a refrence
    summary.

    """
    tokenizer = WordPunctTokenizer()
    candidate = tokenizer.tokenize(candidate.lower())
    reference = tokenizer.tokenize(reference.lower())
    c_ngrams = set(ngrams(candidate, n))
    r_ngrams = set(ngrams(reference, n))
    cr_ngrams = [g for g in c_ngrams if g in r_ngrams]
    rouge_n = len(cr_ngrams) / len(r_ngrams)
    if verbose:
        print("{:d} matching {:d}-grams out of {:d} total.".format(
            len(cr_ngrams), n, len(r_ngrams)))
        print(cr_ngrams)
        print("ROUGE-{:d}: {:0.3f}".format(n, rouge_n))
    return rouge_n


def write_results(results, docids, summarizers):
    """Save the results to a CSV table: rows are documents and columns are
    the different summarization systems.

    """
    csvfile = open("results.csv", "w")
    writer = csv.DictWriter(csvfile, ['docid'] + summarizers)
    writer.writeheader()
    for docid in docids:
        row = {"docid": docid}
        for summarizer in summarizers:
            row[summarizer] = results[(docid, summarizer)]
        writer.writerow(row)
    return


def summarize_results(results, docids, summarizers):
    """Print some summary statistics about the results."""

    # 1. Which system had the best score?
    best = []
    for docid in docids:
        best_score = 0.0
        best_system = "N/A"
        for summarizer in summarizers:
            if results[(docid, summarizer)] > best_score:
                best_score = results[(docid, summarizer)]
                best_system = summarizer
        best.append(best_system)
        
    print("-"*80)
    for summarizer in summarizers:
        best_count = best.count(summarizer)
        best_pct = best_count / len(docids) * 100
        print("{:20s} was the best system {:3d} times ({:2.0f}%).".format(
            summarizer, best_count, best_pct))

    # 2. Mean ROUGE score
    print("-"*80)
    for summarizer in summarizers:
        mean_score = 0.0
        for docid in docids:
            mean_score += results[(docid, summarizer)]
        mean_score = mean_score / len(docids)
        print("{:20s} mean ROUGE score: {:0.4f}".format(
            summarizer, mean_score))
    print("-"*80)
    
    return


def main():
    """This is the main script. It loads each candidate summary, scores it
    with ROUGE-2, and saves the resulting scores to a file on disk.

    """

    dirname = "output"

    # Load the summaries
    print("Loading summaries...")
    docids = set()
    summarizers = set()
    summaries = {}
    for fn in os.listdir(dirname):
        docid, system = fn.split(".")[0].split("-")
        docids.add(docid)
        summarizers.add(system)
        with open(os.path.join(dirname, fn), "r") as f:
            summaries[(docid, system)] = f.read()
    docids = sorted(list(docids))
    summarizers = sorted(list(summarizers))

    # Evaluate each candidate summary
    print("Evaluating summaries...")
    results = {}
    for (docid, system), summary in summaries.items():
        # Load the reference abstract
        absfn = "{:s}-abstract.txt".format(docid)
        with open(os.path.join("cmplg-txt", absfn), "r") as f:
            abstract = f.read()
        results[(docid, system)] = rouge(summary, abstract, n=2)

    # Write the ROUGE results to csv file
    print("Writing evaluation results...")
    write_results(results, docids, summarizers)

    # Display some summary stats about the evaluation
    summarize_results(results, docids, summarizers)

    return


if __name__ == "__main__":
    main()
