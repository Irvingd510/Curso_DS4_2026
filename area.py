"""Calculate the areas of a rectangle given its length and width"""

def calculate_rectange(lenght,width):
    area = lenght * width
    return area
def main():
    """Main function to parse command line arguments and calculate the area"""
    parse = argparse.ArgumentParser(description="Calculate the areas of a rectangle")
    parse.add_argument("-l","Lenght",type=float,help="Lenght of the rectangle")
    parse.add_argument("-w","Width",type=float,help="Width of the rectangle")
    args = parse.parse_args()
    
    area = calculate_rectange(args.Lenght,args.Width)
    print(f"The area of the rectangle with a length of {args.Lenght} and a width of {args.Width} is {area}")

if __name__ == "__main__":
    main()