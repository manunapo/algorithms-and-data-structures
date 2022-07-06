
def isPalindrome(s):
    if len(s) < 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

# returns index if the string is palindrome with just 1 removal,
# returns -1 if it is already a palindrome of if there isnt any removal that makes it pal.


def isPalindromeWithOneError(s):
    ileft = 0
    iright = len(s) - 1
    skips = 0
    skipped_pos = -1
    while ileft < iright and skips <= 1:
        # skipping left to right
        if s[ileft] == s[iright]:
            ileft += 1
            iright -= 1
        elif s[ileft+1] == s[iright]:
            skipped_pos = ileft
            ileft += 1
            skips += 1
        else:
            skipped_pos = -1
            break
    if skips < 2 and skipped_pos != -1:
        return skipped_pos
    else:
        ileft = 0
        iright = len(s) - 1
        skips = 0
        # skipping right to left
        while ileft < iright and skips <= 1:
            if s[ileft] == s[iright]:
                ileft += 1
                iright -= 1
            elif s[ileft] == s[iright-1]:
                skipped_pos = iright
                iright -= 1
                skips += 1
            else:
                skipped_pos = -1
                break
    if skips < 2 and skipped_pos != -1:
        return skipped_pos
    else:
        return -1


def minimumBribes(q):
    total_moves = 0
    for i in range(1, len(q)+1):
        print(f"i: {i}, qi: {q[i-1]}")
        if q[i-1] > i:
            if q[i-1] - i > 2:
                print("Too chaotic")
                return "Too chaotic"
            total_moves += q[i-1] - i
    print(total_moves)


def truckTour(petrolpumps):

    for start in range(len(petrolpumps)):
        print(f"start: {start}")
        cursor = start
        i = 0
        amtPetrol = 0
        while i < len(petrolpumps):
            print(f"-- cursor: {cursor}")
            amtPetrol += petrolpumps[cursor][0]
            if amtPetrol < petrolpumps[cursor][1]:
                break
            elif i == len(petrolpumps) - 1:
                return start
            amtPetrol -= petrolpumps[cursor][1]
            cursor = (cursor + 1) % len(petrolpumps)
            i += 1
    return -1


if __name__ == '__main__':
    test = "aabaa"
    print(f"Is Palindrome {test}: {isPalindrome(test)}")
    test = "aa"
    print(f"Is Palindrome {test}: {isPalindrome(test)}")
    test = "a"
    print(f"Is Palindrome {test}: {isPalindrome(test)}")
    test = "aaaaabaaa"
    print(f"Is Palindrome {test}: {isPalindrome(test)}")

    test = "ac"
    print(
        f"Is PalindromeWithOneError {test}: {isPalindromeWithOneError(test)}")
    test = "aaaaaaaa"
    print(
        f"Is PalindromeWithOneError {test}: {isPalindromeWithOneError(test)}")
    test = "aabbaac"
    print(
        f"Is PalindromeWithOneError {test}: {isPalindromeWithOneError(test)}")
    test = "a"
    print(
        f"Is PalindromeWithOneError {test}: {isPalindromeWithOneError(test)}")
    test = "abca"
    print(
        f"Is PalindromeWithOneError {test}: {isPalindromeWithOneError(test)}")
    test = "abcca"
    print(
        f"Is PalindromeWithOneError {test}: {isPalindromeWithOneError(test)}")
    test = "aaaacc"
    print(
        f"Is PalindromeWithOneError {test}: {isPalindromeWithOneError(test)}")
    test = "hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"
    print(
        f"Is PalindromeWithOneError {test}: {isPalindromeWithOneError(test)}")

    test = [5, 1, 2, 3, 7, 8, 6, 4]
    minimumBribes(test)
    test = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(test)

    test = [[1, 5], [10, 3], [2, 4]]
    print(truckTour(test))
    test = [[5, 5], [2, 3], [20, 4]]
    print(truckTour(test))
