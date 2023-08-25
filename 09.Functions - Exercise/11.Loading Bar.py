def loading_bar(num):
    if num == 100:
        return f"{num}% Complete!" f"\n[{int(num/10) * '%'}]"
    else:
        return f"{num}% [{int(num/10) * '%'}{int((100 - num)/10) * '.'}]" f"\nStill loading..."


print(loading_bar(int(input())))