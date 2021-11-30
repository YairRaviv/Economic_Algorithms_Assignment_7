from typing import List
import copy

#choise rule 1 - choose the top 3 values
def choise_1 (values:list[float])->List[bool]:
    max_1 = -1
    max_2 = -1
    max_3 = -1
    max_1_index = -1
    max_2_index = -1
    max_3_index = -1
    for x in range(0,len(values)):
        if values[x] >= max_1:
            max_3_index = max_2_index
            max_2_index = max_1_index
            max_1_index = x
            max_3 = max_2
            max_2 = max_1
            max_1 = values[x]
        elif values[x] >= max_2:
            max_3_index = max_2_index
            max_2_index = x
            max_3 = max_2
            max_2 = values[x]
        elif values[x] >= max_3:
            max_3_index = x
            max_3 = values[x]
    indexes = {max_1_index,max_2_index,max_3_index}
    answer = []
    for i in range(0,len(values)):
        if i in indexes:
            answer.append(True)
        else:
            answer.append(False)
    return answer

#choise rule 2 - choose top 3 values only if the value >=10
def choise_2 (values:list[float])->List[bool]:
    max_3 = choise_1(values)
    for x in range(0,len(values)):
        if max_3[x] and values[x]<10:
            max_3[x] = False
    return max_3



def payments (values:List[float], choice_rule) -> List[float]:
    """
      >>> test_1 = payments([5,1,4,2,3],choise_1)
      >>> test_1_result =  test_1[0]>=2 and test_1[0]<=2.01 and test_1[1] == 0 and test_1[2]>=2 and test_1[2]<=2.01 and test_1[3] == 0 and test_1[4]>=2 and test_1[4]<=2.01
      >>> test_1_result
      True
      >>> test_2 = payments([1,5,5,1.01],choise_1)
      >>> test_2_result =  test_2[0]==0 and test_2[1]>=1 and test_2[1] <= 1.01 and test_2[2]>=1 and test_2[2]<=1.01 and test_2[3] >=1 and test_2[3]<=1.01
      >>> test_2_result
      True
      >>> test_3 = payments([1,1,1,1],choise_1)
      >>> test_3_result =  test_3[0]==0 and test_3[1]>=1 and test_3[1] <= 1.01 and test_3[2]>=1 and test_3[2]<=1.01 and test_3[3] >=1 and test_3[3]<=1.01
      >>> test_3_result
      True


      >>> test_4 = payments([9,12,14,13],choise_2)
      >>> test_4_result = test_4[0]==0 and test_4[1]>=10 and test_4[1] <= 10.01 and test_4[2]>=10 and test_4[2] <= 10.01 and test_4[3]>=10 and test_4[3] <= 10.01
      >>> test_4_result
      True
      >>> test_5 = payments([7,8,9,0],choise_2)
      >>> test_5_result =  test_5[0]==0 and test_5[1]==0 and test_5[2]==0 and test_5[3]==0
      >>> test_5_result
      True
      >>> test_6 = payments([15,14,13,12],choise_2)
      >>> test_6_result =  test_6[0]>=12 and test_6[0]<=12.01 and test_6[1] >= 12 and test_6[1]<=12.01 and test_6[2]>=12 and test_6[2] <= 12.01 and test_6[3] ==0
      >>> test_6_result
      True



      """

    find_threshold = copy.deepcopy(values)
    final_threshold = copy.deepcopy(values)
    for x in final_threshold:
        x = 0
    n = len(values)

    #find minimum value for each player
    for j in range(0, n):
        if(choice_rule(values))[j]==False:
            continue
        while True:
            tmp = copy.deepcopy(find_threshold)
            tmp[j] = tmp[j]-0.01
            #check if player j passed hid threshold at the last iterate
            if choice_rule(find_threshold)[j] == True and choice_rule(tmp)[j] == False:
                final_threshold[j] = find_threshold[j]
                break
            elif tmp[j]<=0:
                break
            find_threshold = copy.deepcopy(tmp)
    chosen = choice_rule(final_threshold)
    for i in range (0,n):
        if not chosen[i]:
            final_threshold[i]=0

    return final_threshold


if __name__ == '__main__':
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))