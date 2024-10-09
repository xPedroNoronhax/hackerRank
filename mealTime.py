def main():
## pergunte que horas são
    time = input("What time is it? ").strip()
    time = convert(time)

    if time >= 7 and time <=8:
        print("breakfast time")
    elif time >=12 and time <= 13:
        print("lunch time")
    elif time >=18 and time <= 19:
        print("dinner time")
    else:
        0






def convert(time):
    #separe as horas dos minutis
    hours, minutes = time.split(":")
    #deixe horas e minutos em inteiros
    hours = float(hours)
    minutes = float(minutes)
    #converte os minutos para fração
    total_hours = hours + minutes / 60
    return total_hours

main()
