from fuzzywuzzy import fuzz

class Compare():

    def compare_fields(field_1, field_2):
        return fuzz.ratio(field_1,field_2)
    
    def calc_score(scores,fields , flags):
        matching= []
        nMatching = []
        total, matching, nMatching = Compare.calc_fle(scores,flags, matching, nMatching)
        i=0
        while i < len(fields):
            if(scores.get(fields[i])!=''):
                if(scores.get(fields[i])==100):
                    total = total + 1
                    matching.append(fields[i])
                else:
                    total = total - 1
                    nMatching.append(fields[i])
            i= i+1
        return total, matching, nMatching
        
    def calc_fle(scores, flags,matching, nMatching):
        if(flags=='F'):
            if(scores.get('first_name')>80):
                matching.append('first_name')
                return 1, matching, nMatching 
            else:
                nMatching.append('first_name')
                return 0, matching, nMatching
        elif(flags=='L'):
            if(scores.get('last_name')>80):
                matching.append('last_name')
                return 1, matching, nMatching 
            else:
                nMatching.append('last_name')
                return 0, matching, nMatching
        elif(flags=='E'):
            if(scores.get('email')>80):
                matching.append('email')
                return 1, matching, nMatching 
            else:
                nMatching.append('email')
                return 0, matching, nMatching
        elif(flags=='FL' or flags=='LF'):
            if(scores.get('first_name') > 80 and scores.get('last_name') > 80):
                matching.append('first_name')
                matching.append('last_name')
                return 1, matching, nMatching 
            else:
                nMatching.append('first_name')
                nMatching.append('last_name')
                return 0, matching, nMatching
        elif(flags=='FE' or flags=='EF'):
            if(scores.get('first_name') > 80 and scores.get('email') > 80):
                matching.append('first_name')
                matching.append('email')
                return 1, matching, nMatching 
            else:
                nMatching.append('first_name')
                nMatching.append('email')
                return 0, matching, nMatching
        elif(flags=='LE' or flags=='EL'):
            if(scores.get('last_name') > 80 and scores.get('email') > 80):
                matching.append('last_name')
                matching.append('email')
                return 1, matching, nMatching 
            else:
                nMatching.append('last_name')
                nMatching.append('email')
                return 0, matching, nMatching               
        else:
            if(scores.get('first_name') > 80 and scores.get('email') > 80 and scores.get('last_name')>80):
                matching.append('first_name')
                matching.append('last_name')
                matching.append('email')                
                return 1, matching, nMatching 
            else:
                nMatching.append('first_name')
                nMatching.append('last_name')
                nMatching.append('email')
                return 0, matching, nMatching     
