passing_grade=40
a_midterm = float(input("Enter your midterm grade. "))  #  We are taking the grade from the user

a_final= float(input("Enter your final grade. "))  #  We are taking the grade from the user

average = a_midterm * 0.4 + a_final* 0.6

if passing_grade >  average:
    print("YOU SHALL NOT PASS!!!!")
    print("Please take your makeup exam.")
    a_makeup = float(input("Enter your makeup exam."))  # We are taking the grade from the user.
    average = a_midterm * 0.3 + a_final* 0.4 + a_makeup*0.4

else: 
    print("You passed the lesson. Congratulations")


   
if 90 <=  average <= 100:
    print("Your letter grade is AA")
elif 80 <=  average < 90:
    print("Your letter grade is BA")
elif 70 <=  average < 80:
    print("Your letter grade is BB")
elif 60 <=  average < 70:
    print("Your letter grade is CB")
elif 50 <=  average < 60:
    print("Your letter grade is CC")
elif 40 <=  average < 50:
    print("Your letter grade is DC")
elif 30 <=  average < 40:
    print("Your letter grade is DD and you passed conditionally. ")
elif 0 <=  average < 30:
    print("Your letter grade is FF and You have failed.")