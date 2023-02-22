def fileLength(filename):
    try:
    	file = open(filename, 'r')
    	contents = file.read()
    	file.close()
    	print(len(contents))
    except FileNotFoundError:
        print("Error: File " + filename + " not found.")
    except:
        print("Error: Could not read file " + filename + ".")