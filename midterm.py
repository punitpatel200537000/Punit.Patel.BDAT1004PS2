f = open("file.txt", "a")
f.write("Hi, Now the file has more content!")
f.close()

f = open("file.txt", "r")
print(f.read())

"""Lorem ipsum, dolor sit amet consectetur adipisicing elit. Necessitatibus ducimus, quae reprehenderit inventore recusandae laboriosam est vero, beatae molestias quasi accusamus itaque repudiandae dolorem similique id illum vitae laudantium error?"""