from myfunc import add

def main():
    try:
        a=int(input("a="))
        b=int(input("b="))
        result =add(a,b)
        print(f"ผลลัพธ์={result}")
    except ValueError:
        print("กรุณากรอกตัวเลข")
if __name__=="__main__":
    main()
