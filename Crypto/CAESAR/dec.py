
if __name__ == '__main__':
    const = 38

    array_key = [93,42,51,59,9,51,15,88,34,51,2,92,24,51,32,93,26,41,51,24,35,11,95,24,4,95,62,51,27,41,51,88,30,41,51,11,92,93,2,43,51,24,35,51,40,93,9,51,13,32,92,2,9]
    
    for i in range(0,255):
        array_key_sum_dec = []
        array_key_xor_dec = []
        array_key_min_dec = []
        array_key_and_dec = []
        
        sum_ = 0
        min_ = 0
        and_ = 0
        or_ = 0
    
        for num in array_key:
            calc_num = num - i
            array_key_min_dec.append(calc_num)
            
        for num in array_key:
            calc_num = num + i
            array_key_sum_dec.append(calc_num)
            
        for num in array_key:
            calc_num = num & i
            array_key_and_dec.append(calc_num)
            
        for num in array_key:
            calc_num = num ^ i
            array_key_xor_dec.append(calc_num)
        
        for num in array_key_and_dec:
            if (num <= 125 and num >= 33):
                and_+=1
        
        for num in array_key_min_dec:
            if (num <= 125 and num >= 33):
                min_+=1
        
        for num in array_key_sum_dec:
            if (num <= 125 and num >= 33):
                sum_+=1
                
        for num in array_key_xor_dec:
            if (num <= 125 and num >= 33):
                or_+=1
        
        '''print("array and lenght ", len(array_key_and_dec))
        print("and_ val", and_)
        print("array xor lenght ", len(array_key_xor_dec))
        print("xor_ val", or_)
        print("array min lenght ", len(array_key_min_dec))
        print("min_ val", min_)
        print("array sum lenght ", len(array_key_sum_dec))
        print("sum_ val", sum_)'''
        
        str_and = ""
        str_sum = ""
        str_or = ""
        str_min = ""
        
        if (and_ == len(array_key_and_dec)):
            for num in array_key_and_dec:
                str_and = str_and + chr(num)
            and_ = 0
            print("quest è la chiave con somma ", str_and)
            str_and = ""
            
        if (sum_ == len(array_key_sum_dec)):
            for num in array_key_sum_dec:
                str_sum = str_sum + chr(num)
            sum_ = 0
            print("quest è la chiave con somma ", str_sum)
            str_sum = ""
            
        if (min_ == len(array_key_min_dec)):
            for num in array_key_min_dec:
                if (num < 0):
                    continue
                else:
                    str_min = str_min + chr(num)
            min_ = 0
            print("quest è la chiave con somma ", str_min)
            str_min = ""
            
        if (or_ == len(array_key_xor_dec)):
            for num in array_key_xor_dec:
                str_or = str_or + chr(num)
            or_ = 0    
            print("quest è la chiave con somma ", str_or)
            str_or = ""
            
        str_and = ""
        str_sum = ""
        str_or = ""
        str_min = ""
