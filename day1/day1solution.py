import requests

cookies = {'session': '53616c7465645f5f33e74427e67de294e4040e431beb5ec770314600dd15bed6e9abc8513ae620b56c76d931fac2e78481878a5aa0963f6cfe75443539435463'}
webpageRawData = requests.get("https://adventofcode.com/2025/day/1/input", cookies=cookies)

startValue = 50
password = 0
currentValue = startValue




if webpageRawData.status_code == 200:
    eachLineOfData = webpageRawData.text.strip().split("\n")
    for line in eachLineOfData:
        operator = line[0] 
        number = int(line[1:])
        if operator == "R":
            currentValue = (currentValue+number)%100
        elif operator == "L":
            currentValue = (currentValue-number)%100
        print("Current Value after operation", line, "is:", currentValue)
        if currentValue == 0:
            password += 1
        
    print("The password is:", password)
else:
      print("Error: Unable to retrieve data from the webpage. Status code:", webpageRawData.status_code)

