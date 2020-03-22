def printAllKLength(set, k): 
  
    n = len(set)  
    printAllKLengthRec(set, "", n, k) 
  

def printAllKLengthRec(set, prefix, n, k): 
      

    if (k == 0) : 
        print(prefix) 
        return
  

    for i in range(n): 
  

        newPrefix = prefix + set[i] 
          
        printAllKLengthRec(set, newPrefix, n, k - 1) 
  

if __name__ == "__main__": 
      
    print("---------Created By: H A C K Z E E E---------") 
    set1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', '%', '-']
    k = 2
    printAllKLength(set1, k) 
