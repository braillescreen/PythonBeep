import winsound, time
print("Okay, atempting to print the terminal bell.")
input()
print("\a")
print("Now doing a winsound beep.")
input()
winsound.Beep(1000,1000)
print("Okay, now doing a thing where we go through a loop and beep.")

for x in range(37, 2000, 49):
	if x<37: continue
	winsound.Beep(x,200)
