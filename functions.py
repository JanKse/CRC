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
 
    checkword = tmp
    return checkword
 

# function to encode the data
def encodeData(data, key):
 
    # Appends n-1 zeroes at end of data; n = length of key
    appended_data = data + '0'*(len(key)-1)
   
    remainder = binDiv(appended_data, key)
 
    # Append remainder in the original data
    codeword = data + remainder
    return codeword   
print(encodeData('100010110101101001110','1001'))