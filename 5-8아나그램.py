import sys
sys.stdin = open("input.txt", "r")

word1 = list(input())
word2 = list(input())
word1_dic = dict()
word2_dic = dict()

for i in range(len(word1)):
    if word1[i] in word1_dic:
        word1_dic[word1[i]] += 1
    else:
        word1_dic[word1[i]] = 1
    if word2[i] in word2_dic:
        word2_dic[word2[i]] += 1
    else:
        word2_dic[word2[i]] = 1

if word1_dic == word2_dic:
    print("YES")
else:
    print("NO")