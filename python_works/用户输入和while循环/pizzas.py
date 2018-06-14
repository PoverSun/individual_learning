pizza =  "\nPleasse input the pizza\'s consists: "

pizza += "\nEnter 'quit' to end the progame. "

list1 = ''
while list1 != 'quit':
      list1 = input(pizza)

      if list1 != 'quit':
            print("\n我们会在pizza中加 "+list1+ "这种料的。")
      else:
            print("\n退出")
