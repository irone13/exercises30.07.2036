cooking = int(input("How much time to bring the meal ? (in minute)"))
price = int(input("How much does the meal cost ? (shekels)"))
is_quick_service = cooking < 15
is_expensive = price > 100
if is_quick_service and not is_expensive:
    print ("Recommended")
else :
    print ("Not recommended")













