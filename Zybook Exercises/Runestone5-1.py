def ispalindrome(refstring):
    if (refstring == refstring[::-1]) and len(refstring) >=3:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    ispalindrome("rr")