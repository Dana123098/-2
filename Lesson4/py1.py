mashin=["bmv","mz","ac"]
print(mashin[0].title())

print(mashin[-1])
message = f"я не хо. р. эту марку {mashin[1].title()} дайте без нее"
print(message)
del_item=mashin.pop(0)
print(mashin)

mashin.insert(0 , "su")
mashin.insert(2 , "kkk")
print(mashin)
del mashin[2]
print(mashin)

mashin.append("jghj")
print(mashin)
