https://github.com/sharmas01/Messycode.git

def arithmetic_arranger(*problems):
  prob_string = problems[0]  #string of problems  
  if len(prob_string) > 5:
        return 'Error: Too many problems.'  #catch none also
    #split all problem string into list of  triplets ['digit','operator','digit'] if valid
  prob_str_list = []
  arranged_problems=''
  for p in prob_string:
    p_list = p.split(' ')
    print(p_list)
    if p_list[1] not in ['+','-']:
      return "Error: Operator must be '+' or '-'."
    elif not p_list[0].isdigit() or not p_list[2].isdigit():
      return "Error: Numbers must only contain digits."
    elif len(p_list[0]) > 4 or len(p_list[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
      
    prob_str_list.append(p_list)
    max_len=max(len(p_list[0]),len(p_list[2]))
    if not problems[1:]:
      if arranged_problems == '':
        arranged_problems=p_list[0].rjust(max_len+2)+'\n'+p_list[1]+p_list[2].rjust(max_len+1)+'\n'+ (max_len+2)*'-'
      else:  
        linebreak_pos=[pos for pos, char in enumerate(arranged_problems) if char == '\n']
        arranged_problems = arranged_problems[0:linebreak_pos[0]]+' '*5+p_list[0].rjust(max_len+1)+ arranged_problems[linebreak_pos[0]:linebreak_pos[1]] +' '*4 + p_list[1] +p_list[2].rjust(max_len+1)+arranged_problems[linebreak_pos[1]:]+' '*4 + (max_len+2)*'-'
    else:
      if arranged_problems == '':
        a=int(p_list[0])
        b=int(p_list[2])
        arranged_problems=p_list[0].rjust(max_len+2)+'\n'+p_list[1]+p_list[2].rjust(max_len+1)+'\n'+ (max_len+2)*'-'+'\n'+str(a+b if p_list[1]=='+' else a-b).rjust(max_len+2)
      else:
        a=int(p_list[0])
        b=int(p_list[2])
        linebreak_pos=[pos for pos, char in enumerate(arranged_problems) if char == '\n']
        print(linebreak_pos)
        arranged_problems = arranged_problems[0:linebreak_pos[0]]+' '*5 + p_list[0].rjust(max_len+1)+ arranged_problems[linebreak_pos[0]:linebreak_pos[1]] +' '*4 + p_list[1] +p_list[2].rjust(max_len+1)+arranged_problems[linebreak_pos[1]:linebreak_pos[2]]+' '*4 + (max_len+2)*'-' +arranged_problems[linebreak_pos[2]:] +'    '+str(a+b if p_list[1]=='+' else a-b).rjust(max_len+2)
  print(arranged_problems)  
  return arranged_problems
