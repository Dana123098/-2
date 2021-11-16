prompt = "\n Что хотите на пицце"
prompt += "\nВведите “quit” для завершения программы : "

message = ""
while message != "quit":
   message = input(prompt)
   print("включено", message)

