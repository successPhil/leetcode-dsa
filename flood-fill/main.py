def hello_world():
    return "Hello World!"


def floodFill(image, sr, sc, color):
    starting_color = image[sr][sc]

    if starting_color == color:
        return image
    
    def recursive_fill(r,c):
        if 0 <= r < len(image[0]) and 0 <= c < len(image[0]) and image[r][c] == starting_color:
            image[r][c] = color

            recursive_fill(r - 1, c)
            recursive_fill(r + 1, c)
            recursive_fill(r, c - 1)
            recursive_fill(r, c + 1)
        
    recursive_fill(sr,sc)
    return image





    
 

    

    




if __name__ == '__main__':
    print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))