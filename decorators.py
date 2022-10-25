def batch(arg):
    print("Now checking data availability")
    return arg

@batch
def data_available():
    lhr = int(input("is Lahore data available?, 0/1:"))
    islmbd = int(input("is Islamabad data available?, 0/1:"))
    khi = int(input("is Karachi data available?, 0/1:"))

    if lhr == 0 or islmbd == 0 or khi == 0:
        print("Data is not available")
    else:
        print("Load in processing")

data_available()


if __name__=="__main__":
    print("you are in main")
else:
    print("you are not in main")