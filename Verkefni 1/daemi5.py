secs_str = input("Input seconds: ") # do not change this line
hours = int(secs_str) // 3600
minutes = int(secs_str)/60 - hours*60
minutes = int(minutes)
seconds = int(secs_str)-hours*3600-minutes*60
seconds = int(seconds)
print(hours,":",minutes,":",seconds) # do not change this line