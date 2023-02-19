# python3


from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
            # Process opening bracket, write your code here
            

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
            
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position
    return "Success"
            # Process closing bracket, write your code here
        


def main():
    # print("ievadi I vai F: ")
    text = input()
    if text == "I":
        # print("Kods: ")
        tex2 =input()
        mismatch = find_mismatch(tex2)
        print(mismatch)
    elif text == "F":
        # print("ievadi faila nr. no 0 līdz 5: ")
        failins= input()
        failins1 = int(failins)
        if failins1 >= 0 and failins1 < 5:
            file = open(failins1, "r")
            tex3 = file.read()
            print(tex3)
            file.close()
            
            mismatch = find_mismatch(tex3)
            print(mismatch)
        else:
            print("nekorekta ievade")



        
        


    
    
    # Printing answer, write your code here



if __name__ == "__main__":
    main()
