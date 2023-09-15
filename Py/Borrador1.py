def Schedule_Class(Num, Classes, Hours, Teachers, Themes):
    Schedule = []
    index = 0
    while index < len(Num):
        Scheduled = "The " + Num[index] + " class is " + Classes[index] + " at " + Hours[index] + " With " + Teachers[index] + " and we're studing " + Themes[index] 
        Schedule.append(Scheduled)
        index += 1

    return Schedule


Schedule_Num = ["1th", "2nd", "3rd", "4th", "5th"]
Schedule_Classes = ["Math", "Lenguage", "Physics", "Chemistry", "Music"]
Schedule_Hours = ["7:00", "8:00", "9:00", "10:00", "11:00"]
Teachers_Classes = ["Mrs. Beth", "Mrs. Jaymes", "Mrs. Kaori", "Mrs. Jude", "Mrs.Taylor"]
Schedule_Themes = ["Algebra", "Spanish", "1.th law of newton", "Organic", "Gyonopedia"]

schedule = Schedule_Class(Schedule_Num, Schedule_Classes, Schedule_Hours, Teachers_Classes, Schedule_Themes)
print(f"Monday schedule: {schedule}")

