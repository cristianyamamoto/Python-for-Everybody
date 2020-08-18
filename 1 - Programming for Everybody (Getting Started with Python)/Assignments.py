# print('Hello, I\'m Cristian Yamamoto')

# # Assignment 2.3
# hrs = input("Enter Hours:")
# rate = input("Enter rate:")
# print("Pay:", float(hrs) * float(rate))


# # Assignment 3.1
# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input("Enter rate:")
# r = float(rate)

# if h < 40:
#     print(h * r)
# else:
#     additionalHrs = h - 40
#     print(((additionalHrs*1.5) + 40) * r)


# # Assignment 3.2
# score = input("Enter Score: ")
# score = float(score)

# if score >= 0.9:
#     print("A")
# elif score >= 0.8:
#     print("B")
# elif score >= 0.7:
#     print("C")
# elif score >= 0.6:
#     print("D")
# elif score < 0.6:
#     print("F")
# elif 0.0 < score < 1.0:
#     print("The score is out of range!")

# # Assignment 4.6
# def computepay(hrs, rate):
# 	h = float(hrs)
# 	r = float(rate)

# 	if h <= 40:
# 	    return(h * r)
# 	else:
# 	    additionalHrs = h - 40
# 	    return(((additionalHrs*1.5) + 40) * r)
    

# hrs = input("Enter Hours:")
# rate = input("Enter rate:")
# p = computepay(hrs, rate)
# print("Pay",p)

# # Assignment 5.2
# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done" : break
        
#     try:
#         number = int(num)
#     except:
#         print("Invalid input")
        
#     if largest is None:
#         largest = number
#     elif number > largest:
#         largest = number
    
#     if smallest is None:
#         smallest = number
#     elif number < smallest:
#         smallest = number
        
    
    

# print("Maximum is", largest)
# print("Minimum is", smallest)