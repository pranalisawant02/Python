#Q4.Counting Passengers in a Bus

stop=1
Total_pass=0
while(stop<=5):
  n=int(input(f"Enter the no of passengers at stop { stop} :"))
  Total_pass=Total_pass+n
  stop=stop+1
print("Total passengers = ",Total_pass)
