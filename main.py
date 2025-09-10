from myfunc import add

def main():
    try:
        a=float(intput("a="))
        b=float(intput("b="))
    result =add(a,b)
    print(f"ผลลัพธ์={result}")
    except ValueError:
if __name__=="__main__":
    main()
