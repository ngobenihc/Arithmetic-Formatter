def arithmetic_arranger(problems, arrange_str_num = False):
    
    
 
  if len(problems) > 5 :
    return('Error: Too many problems.')

  
  four_digits = list()
  space_operators = list()
  operators = list()
  numnber = list()
  false_line_space = str()
  line_space = str()
  true_line_space = str()
  all_line_space = str()


  
  for hc in problems:
    hc.lstrip()
    hc.rstrip()
    sproblem = hc.split(" ")
    if len(sproblem[0]) > 4 or len(sproblem[2]) > 4:
      return('Error: Numbers cannot be more than four digits.')
    if not (sproblem[1] == '+' or sproblem[1] == '-'):
      return('Error: Operator must be \'+\' or \'-\'.') 
    four_digits.append(sproblem[0])
    operators.append(sproblem[1])
    space_operators.append(sproblem[2])

  
  counter = 0
  while counter < len(problems):
    try:
      a = int(four_digits[counter])
      b = int(space_operators[counter])
    except:
      return('Error: Numbers must only contain digits.')
    if operators[counter] == '+':
      numnber.append(str(a + b))
    elif operators[counter] == '-':
      numnber.append(str(a - b))
    
    #Finding the width of longest operand
    long = max(len(four_digits[counter]), len(space_operators[counter]))

    
    for h in range((long + 2) - len(four_digits[counter])):
      four_digits[counter] = ' ' + four_digits[counter]
    false_line_space = false_line_space + four_digits[counter] + '    '

    
    for h in range((long + 1)- len(space_operators[counter])):
      space_operators[counter] = ' ' + space_operators[counter]
    line_space = line_space + operators[counter] + space_operators[counter] + '    '

    
    for h in range(long + 2):
      true_line_space = true_line_space + '-'
    true_line_space = true_line_space + '    '

    
    for h in range((long + 2) - len(numnber[counter])):
      numnber[counter] = ' ' + numnber[counter]
    all_line_space = all_line_space + numnber[counter] + '    '

    counter = counter + 1

  
  false_line_space = false_line_space.rstrip()
  line_space = line_space.rstrip()
  true_line_space = true_line_space.rstrip()
  all_line_space = all_line_space.rstrip()
  if arrange_str_num == False:
    arranged_problems = false_line_space + '\n' + line_space + '\n' + true_line_space
  elif arrange_str_num == True:
    arranged_problems = false_line_space + '\n' + line_space + '\n' + true_line_space + '\n' + all_line_space
  
  return arranged_problems