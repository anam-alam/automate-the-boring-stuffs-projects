
def list_to_str(li):

    output_str = ''
    length = len(li)
    
    if length == 1:
        output_str = li[0]
    
    elif length == 2:
        output_str = li[0] + ' and ' + li[1]  
        
    else:
        for i in range(length):
            if i != length - 1:
                output_str += str(li[i]) + ', '
            else:
                output_str += 'and ' + str(li[i])
                
    return output_str

if __name__ == '__main__':
    #spam = ['apples', 'bananas', 'tofu', 'cats']
    spam = [1,2,3,4]
    #spam = ['apples', 'tofu']
    print(list_to_str(spam))
