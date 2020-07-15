deg, dis = map(int, input().split())
deg = deg / 10
dir = ""
dirl = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", 
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
wind = [[0.0, 0.24], [0.25, 1.54], [1.55, 3.34], [3.35, 5.44], [5.45, 7.94],
        [7.95, 10.74], [10.75, 13.84], [13.85, 17.14], [17.15, 20.74], [20.75, 24.44],
        [24.45, 28.44], [28.45, 32.64], [0, 0]]
w = 0

for i in range(15):
    upper = 348.75 - i * 22.5
    lower = upper - 22.5
    if deg >= lower and deg < upper:
        res = 15 - i
        break
    else:
        res = 0

for i in range(13):
    w = i
    #print(i, float(wind[i][0]) * 60, float(wind[i][1]) * 60)
    #print(i, float(wind[i][0]) * 60 <= dis, dis <= float(wind[i][1]) * 60)
    if float(wind[i][0]) * 60 <= dis and dis <= float(wind[i][1]) * 60:
        break


if w == 0:
    dir = "C"
else:
    dir = dirl[res]

print("{} {}" .format(dir, w))