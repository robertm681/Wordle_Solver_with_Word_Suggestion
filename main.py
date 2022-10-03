def Yellow_Letter():
  YT = int(input('Number of Yellow Letters: '))

  if YT == 0:
    with open('Words_0.txt') as file:
      for line in file:
        file = open('Words_1.txt', "a+")
        file.write(str(line))
        file.close()
      
  if YT > 0:
    YLP = int(input('Position of the Yellow Letter(s): '))
    YLP = YLP - 1
    YT = YT - 1
    with open('Words_0.txt') as file:
      Yellow_Letter = input('Enter Yellow Letter: ')
      for line in file:
        if Yellow_Letter in line[YLP]:
          pass
        elif Yellow_Letter in line:
          file = open('Words_1.txt', "a+")
          file.write(str(line))
          file.close()
          
    while YT > 0:
      YT = YT - 1
      YLP = int(input('Position of the Yellow Letter(s): '))
      YLP = YLP - 1
      
      with open('Words_1.txt') as file:
        Yellow_Letter = input('Enter Yellow Letter: ')
        for line in file:
          if Yellow_Letter in line[YLP]:
            pass
          elif Yellow_Letter in line:
            file = open('Words_2.txt', "a+")
            file.write(str(line))
            file.close() 
    
      with open('Words_1.txt') as file:
        file = open('Words_1.txt', "w+")
        file.truncate(0)
        file.close()
    
      with open('Words_2.txt') as file:
        for line in file:
          file = open('Words_1.txt', "a+")
          file.write(str(line))
          file.close()
    
      with open('Words_2.txt') as file:
        file = open('Words_2.txt', "w+")
        file.truncate(0)
        file.close()
        
Yellow_Letter()

def Green_Letter(): 
  GT = int(input('Number of Green Letters: '))

  if GT == 0:
    with open('Words_1.txt') as file:
      for line in file:
        file = open('Words_2.txt', "a+")
        file.write(str(line))
        file.close()
        
  if GT > 0:
    GLP = int(input('Position of the Green Letter(s): '))
    GLP = GLP - 1
    GT = GT - 1
    with open('Words_1.txt') as file:
      Green_Letter = input('Enter Green Letter: ')
      for line in file:
        if Green_Letter in line[GLP]:
          file = open('Words_2.txt', "a+")
          file.write(str(line))
          file.close()
        
  while GT > 0:
    GT = GT - 1
    GLP = int(input('Position of the Green Letter(s): '))
    GLP = GLP - 1
    
    with open('Words_2.txt') as file:
      Green_Letter = input('Enter Green Letter: ')
      for line in file:
        if Green_Letter in line[GLP]:
          file = open('Words_3.txt', "a+")
          file.write(str(line))
          file.close()
  
    with open('Words_2.txt') as file:
      file = open('Words_2.txt', "w+")
      file.truncate(0)
      file.close()
  
    with open('Words_3.txt') as file:
      for line in file:
        file = open('Words_2.txt', "a+")
        file.write(str(line))
        file.close()
  
    with open('Words_3.txt') as file:
      file = open('Words_3.txt', "w+")
      file.truncate(0)
      file.close()
      
Green_Letter()

def Grey_Letter():
  GrT = int(input('Number of Grey Letters: '))
  
  if GrT > 0:
    GrT = GrT - 1
    with open('Words_2.txt') as file:
      Grey_Letter = input('Enter Grey Letter: ')
      for line in file:
        if Grey_Letter in line:
          pass

        else:
          file = open('Words_3.txt', "a+")
          file.write(str(line))
          file.close()
        
  while GrT > 0:
    GrT = GrT - 1
    
    with open('Words_3.txt') as file:
      Grey_Letter = input('Enter Grey Letter: ')
      for line in file:
        if Grey_Letter in line:
          pass

        else:
          file = open('Words_4.txt', "a+")
          file.write(str(line))
          file.close()
  
    with open('Words_3.txt') as file:
      file = open('Words_3.txt', "w+")
      file.truncate(0)
      file.close()
  
    with open('Words_4.txt') as file:
      for line in file:
        file = open('Words_3.txt', "a+")
        file.write(str(line))
        file.close()
  
    with open('Words_4.txt') as file:
      file = open('Words_4.txt', "w+")
      file.truncate(0)
      file.close()

Grey_Letter()

"""def Count():
  z = 0
  with open('Words_3.txt') as file:
    for line in file:
      i = 97
      word_total = 0
      #for line in file:
      while i < 123:
        l = chr(i)
        i = i + 1
  
        file = open('Words_3.txt', "r")
        data = file.read()
        occurance = data.count(l)
  
        if occurance > 0:
          #print(l, "=", occurance)
          word_1 = l[0]
          #print(word_1)
          x = 0
          while x < 5:
            if word_1 in line[x]:
              word_total = word_total + occurance
            x = x + 1
  
      z = z + 1  
      print(z, word_total)
Count()"""

def Improved_Count():
  with open('Words_3.txt') as file:
    for line in file:
      i = 97
      
      while i < 123:
        l = chr(i)
        i = i + 1
        
        file = open('Words_3.txt', "r")
        file.read()
        
        if l in line:
          file = open('Words_4.txt', "a+")
          file.write(str(l))
          file.close

  word_total = 0
  x = 0

  with open('Words_3.txt') as file:
    for line in file:
      x = 97
    
      while x < 123:
        w = chr(x)
        x += 1
        
        file = open('Words_4.txt', "r")
        data = file.read()  
        count = data.count(w)
  
        if w in line:
          word_total = word_total + count
          
      file = open('Words_5.txt', "a")
      file.write(str(word_total))
      file.write(str(" = "))
      file.write(str(line))

      file = open('Words_6.txt', "a")
      file.write(str("\n"))
      file.write(str(word_total))
      file.write(str("\n"))
      file.close()
      
      word_total = 0                        #Resets value stored in word_total

  
  highest_value = 0
  
  with open('Words_6.txt') as file:
    for line in file:
      data = file.readline()
      data = int(data)

      if data > highest_value:  
        highest_value = data

      else:
        pass

  
  highest_value = str(highest_value)

  with open('Words_5.txt') as file:
    for line in file:
      if highest_value in line:
        print(line)
      
Improved_Count()

def Clear():                                                          # Clears all existing files for next guess

  Done = print(input('Hit any key to restart'))
  
  with open('Words_1.txt') as file:
    for line in file:
      file = open('Words_1.txt', "a+")
      file.truncate(0)
      file.close
      
  with open('Words_2.txt') as file:
    for line in file:
      file = open('Words_2.txt', "a+")
      file.truncate(0)
      file.close

  with open('Words_3.txt') as file:
    for line in file:
      file = open('Words_3.txt', "a+")
      file.truncate(0)
      file.close
      
  with open('Words_4.txt') as file:
    for line in file:
      file = open('Words_4.txt', "a+")
      file.truncate(0)
      file.close
      
  with open('Words_5.txt') as file:
    for line in file:
      file = open('Words_5.txt', "a+")
      file.truncate(0)
      file.close
      
  with open('Words_6.txt') as file:
    for line in file:
      file = open('Words_6.txt', "a+")
      file.truncate(0)
      file.close

Clear()
