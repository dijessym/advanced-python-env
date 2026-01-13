# ===== DILYAZ STYLE =====

import string

dword_freq = {}
dlines_count = 0
dwords_count = 0

with open("text.txt", "r", encoding="utf-8") as dfile:
    for dline in dfile:
        dlines_count += 1

        dline = dline.lower()
        for dch in string.punctuation:
            dline = dline.replace(dch, "")

        dwords = dline.split()
        dwords_count += len(dwords)

        for dword in dwords:
            if dword in dword_freq:
                dword_freq[dword] += 1
            else:
                dword_freq[dword] = 1

with open("analysis.txt", "w", encoding="utf-8") as dout:
    dout.write(f"Total lines: {dlines_count}\n")
    dout.write(f"Total words: {dwords_count}\n")
    dout.write("Word frequency:\n")

    for dword in dword_freq:
        dout.write(f"{dword}: {dword_freq[dword]}\n")
