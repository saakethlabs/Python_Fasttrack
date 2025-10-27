# Enter the money received and output the number of cupcakes that can be served
# Assume price of cupcakes to be 2.5

# 20$
# 8

input_money = input("Please enter the received amount:")

input_money = float(input_money) # str -> float

no_cup_cakes = input_money // 2.5 # Integer division
# no_cup_cakes = int(no_cup_cakes) # float -> int

print(f"You will receive {no_cup_cakes} cup cakes")