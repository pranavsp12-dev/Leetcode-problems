/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int* findAnagrams(char* s, char* p, int* returnSize) {

    int n = strlen(s);
    int k = strlen(p);

    int *result = (int *)malloc(n * sizeof(int));
    *returnSize = 0;

    if (k > n)
        return result;

    int freqP[26] = {0};
    int freqS[26] = {0};

    // Frequency of pattern
    for (int i = 0; i < k; i++)
        freqP[p[i] - 'a']++;

    // Frequency of first window
    for (int i = 0; i < k; i++)
        freqS[s[i] - 'a']++;

    // Check first window
    bool same = true;

    for (int i = 0; i < 26; i++) {
        if (freqP[i] != freqS[i]) {
            same = false;
            break;
        }
    }

    if (same) {
        result[*returnSize] = 0;
        (*returnSize)++;
    }

    int left = 0;

    // Slide the window
    for (int right = k; right < n; right++) {

        freqS[s[left] - 'a']--;
        freqS[s[right] - 'a']++;

        left++;

        same = true;

        for (int i = 0; i < 26; i++) {
            if (freqP[i] != freqS[i]) {
                same = false;
                break;
            }
        }

        if (same) {
            result[*returnSize] = left;
            (*returnSize)++;
        }
    }

    return result;
}