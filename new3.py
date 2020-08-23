def carParkingRoof(cars, k):
    # Write your code here
    car_sort=sorted(cars)
    i=0
    min_length=car_sort[-1]
    while i <= len(cars)-k:
        temp=car_sort[i+k-1]-car_sort[i]+1
        if temp<min_length:
            min_length=temp
        i=i+1
    return min_length



carParkingRoof([1,5,3,4,2],2)