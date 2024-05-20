def display(area):
    print(f"The area is {area}")

def get_input():
    received_length = input ("Length:")
    recived_width = input ("width:") 
    return (received_length, recived_width)

def compute_area(length,width):
    area=int(length)* int(width)
    return (area)
def main():
    (length, width)= get_input()

    area= compute_area(length,width)
    display (area)

    
    
main()
