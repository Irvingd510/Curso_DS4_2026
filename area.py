"""Calculate the areas of a rectangle given its length and width"""

def calculate_rectange(lenght,width):
    area = lenght * width
    return area
def main():
    parse = argparse.ArgumentParser(description="Calculate the areas of a rectangle")
    parse.add_argument("Lenght",type=float,help="Lenght of the rectangle")
    parse.add_argument("Width",type=float,help="Width of the rectangle")
    args = parse.parse_args()
    area = calculate_rectange(args.Lenght,args.Width)
    print(f"The area of the rectangle with a length of {args.Lenght} and a width of {args.Width} is {area}")