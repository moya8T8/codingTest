#프로그래머스 K번째수 
def solution(array, commands):
    
    answer = []
    arrays = []
    
    for i in range(len(commands)):
        for j in range(commands[i][0]-1, commands[i][1]):
            
            arrays.append(array[j])
            arrays.sort()   
        answer.append(arrays[commands[i][2]-1])
        arrays = []          
    return answer
