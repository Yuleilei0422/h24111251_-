v=float(input("Input velocity:"))
c=299792458
light_speed = (v/c)
print("Percentage of light speed =",light_speed)
r=1/(1-(v*v)/(c*c))**0.5
AlphaCentauri=4.3
time1=AlphaCentauri/r
print("Time to Alpha Centauri =",time1)
BarnardsStar=6.0
time2=BarnardsStar/r
print("Time to Barnards Star =",time2)
Betelgeuse=309
time3=Betelgeuse/r
print("Time to Betelgeuse (in the Milky Way) =",time3)
AndromedaGalaxy=2000000
time4=AndromedaGalaxy/r
print("Time to Andromeda Galaxy (closest galaxy) =",time4)
