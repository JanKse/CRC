from numpy import divide, remainder, zeros, array, insert, mod, floor, power, arange, polydiv
from numpy.core.arrayprint import array2string
from numpy.lib.function_base import append

def stringXOR(a, b):
    # initialize result
    result = ''
    # if bits are same, then stringXOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
           result += '0'
        else:
            result += '1'
    return result
 
# Binary division function
def binDiv(divident, divisor):
 
    # Number of bits to be sxored at a cycle
    pick = len(divisor)
    tmp = divident[0 : pick]
    while pick < len(divident):
        if tmp[0] == '1':
            tmp = stringXOR(divisor, tmp) + divident[pick]
        else: 
            tmp = stringXOR('0'*pick, tmp) + divident[pick]
        # increment pick to move further
        pick += 1

    if tmp[0] == '1':
        tmp = stringXOR(divisor, tmp)
    else:
        tmp = stringXOR('0'*pick, tmp)
 
    result = tmp
    return result
 

# function to encode the data
def encodeData(data, key):
    # Appends n-1 zeroes at end of data

    appendedData = data + '0'*(len(key)-1)
    remainder = binDiv(appendedData, key)
    # Append remainder in the original data
    codeword = data + remainder
    return codeword   

def decodeData(data, key):

    
    remainder = binDiv(data, key)
    
    return remainder ,data[:len(data) - (len(key) -1)]

    #Convert decimal numbers to
    # binary numbers with Left-MSB orientation 
def decToBin(d,n):

    result = mod(floor(d*power(2,arange(1-n,1.0))),2)
    return result


def cyclepoly(n,k):

    genDegree = n-k

    nn = 2**(genDegree-1) -1 

    
    pp = array([1,1])
    pp = insert(pp, 1, zeros(n-1))

    strPp= ''.join(str(x) for x in pp)
    
    
    print(strPp)
    
    tmp = []
    result=[]
    for x in range(nn):
        test = array([1,1])
        test = insert(test,1, decToBin(x,genDegree-1))
        strTest = ''.join(str(i) for i in test)
        tmp.append(binDiv(strPp,strTest))

        if int(tmp[x],2) ==0 :
           result.append(strTest)
        
        
        #print(rx)
    
    print(result)