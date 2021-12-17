dict={"a":1, "b":2, "c":3, "d":4}
x={i:"even" if dict[i]%2==0 else "odd" for i,j in dict.items()}
