def main(n,k, current_string=""):
    if len(current_string)==n:
        final_sol.append(current_string)
        return

    
    for i in range(k):
        current_string+=str(i)
        main(n,k, current_string)
        current_string = current_string[:-1]
    
    return



if __name__=="__main__":
    final_sol = []
    main(4,3)
    print(final_sol)