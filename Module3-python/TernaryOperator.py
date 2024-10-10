# value_if_true if condition ele value_if_false
mark=60
result="pass" if(mark>50) else"fail"
print("type1 result for ternary operator:"+result)

# if-> else(if&else)
mark=60
result="fail" if(mark<50) else "outstanding" if (mark>90) else"Average"
print("type2 result for ternary operator:"result)
