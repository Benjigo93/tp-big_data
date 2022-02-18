import time
from mrjob.job import MRJob

# PYTHON
# Execution => 0.24 s
with open('vhugo.txt', encoding="UTF-8") as f:
    lines = f.read()


def countWords(f):
    words = {}
    for i in f.split():
        if i not in words:
            words[i] = 1
        else:
            words[i] += 1

    return words


start = time.time()
print(countWords(lines))
duration = time.time() - start
print("{:.2f}".format(duration) + " s")


# MRJOB
# Execution => 3.08 s
class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            for char in [",", ".", ",", "\u00ea"]:
                if char in word and char != "\u00ea":
                    word = word.replace(char, "")
                else:
                    word = word.replace(char, "é")
            if len(word) >= 3:
                yield (word, 1)

    def reducer(self, key, values):
        yield key, sum(values)


start = time.time()
if __name__ == '__main__':
    MRWordFrequencyCount.run()
duration = time.time() - start
print("{:.2f}".format(duration) + " s")

# conclusion: Le programme écrit avec du PYTHON core est beaucoup plus rapide que le programme écrit avec MRJob.
