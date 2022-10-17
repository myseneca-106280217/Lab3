A function that will write a text file to your PC with your name:
  
#!/usr/bin/env python3

#defining a function in which we further open the file and write name in it, and then closing the file.
def put_a_name_to_file():
    f = open("name.txt" , "w+")
    f.write("Mehak Preet Singh")
    f.close()
    
if __name__ == "__main__":
    put_a_name_to_file()
