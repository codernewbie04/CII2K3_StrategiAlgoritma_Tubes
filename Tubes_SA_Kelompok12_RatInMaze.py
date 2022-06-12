import time
import itertools
 
# Print maze (agar bentuknya rapih)
def printSolution( sol ):
     
    for i in sol:
        for j in i:
            print(str(j) + " ", end ="")
        print("")
 
# Melakukan pengecekan apakah x,y valid
# untuk index N x N Maze
def isSafe( maze, x, y ):
     
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
     
    return False
 
""" Fungsi mengembalikan false jika tidak ada jalur yang memungkinkan, jika ada melakukan penelusuran rute, dan jika jalur buntu akan melakukan backtracking """
def solveMaze( maze, N):
     
    # Membuat NxN 2D list
    sol = [ [ 0 for j in range(N) ] for i in range(N) ]
     
    if solveMazeUtil(maze, 0, 0, sol, N) == False:
        print("Solusi Tidak tersedia")
        return False
    #print(sum([sum(i) for i in zip(*sol)]))
    print("With Backtracking Algorithm")
    printSolution(sol)
    return True
     
# Fungsi rekursif untuk mencari jalan keluar (mencari solusi)
def solveMazeUtil(maze, x, y, sol, N):
     
    # jika(x, y adalah tujuan (rute keluar berada di pojok kanan bawah (N-1, N-1))) mengembalikan true
    if x == N - 1 and y == N - 1 and maze[x][y]== 1:
        sol[x][y] = 1
        return True
         
    # Check apakah maze[x][y] valid ?
    if isSafe(maze, x, y) == True:
        # Apakah blok yang saat ini ditempati sudah menjadi solusi (dilakukan pengecekan pada list sol)
        if sol[x][y] == 1:
            return False
           
        # Menandai jalur yang sedang dilalui dengan 1 (1 : jadi jalur solusi, 0 : bukan jalur solusi)
        sol[x][y] = 1
         
        # Maju ke arah x 
        if solveMazeUtil(maze, x + 1, y, sol, N) == True:
            return True
             
        # Jika bergerak dalam arah x tidak memberikan solusi maka Bergerak ke bawah dalam arah y
        if solveMazeUtil(maze, x, y + 1, sol, N) == True:
            return True
           
        # Jika bergerak ke arah y tidak memberikan solusi maka Kembali ke arah x
        if solveMazeUtil(maze, x - 1, y, sol, N) == True:
            return True
             
        # Jika bergerak mundur dalam arah x tidak memberikan solusi maka Bergerak ke atas dalam arah y
        if solveMazeUtil(maze, x, y - 1, sol, N) == True:
            return True
         
        # Jika tidak ada gerakan di atas yang berhasil maka
        # BACKTRACK: hapus tanda x, y sebagai bagian dari jalur solusi
        sol[x][y] = 0
        return False


def sum_path(path):
    return sum([sum(i) for i in zip(*path)])

# Melakukan filtering untuk blok x,y yang bernilai 1 pada solusi, tetapi pada maze bernilai 0
def isAccepted(maze, solution):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 0:
                if solution[i][j] == 1:
                    return False
    return True


# Melakukan pengecekan apakah rute start terhubung dengan jalur keluar
def isAccepted2(solution, N):
    sol = [ [ 0 for j in range(N) ] for i in range(N) ]
    return solveMazeUtil(solution, 0, 0, sol, N)

def solveWithBF(maze, N):
    list_of_solution = []
    for i in itertools.product([0, 1], repeat=N*N):
        sol= [list(i)[x:x+N] for x in range(0, len(list(i)), N)]
        if isAccepted(maze, sol) and isAccepted2(sol, N):
            list_of_solution.append(sol)
    
    sorted(list_of_solution, key=sum_path)
    print("With Bruteforce Algorithm")
    printSolution(list_of_solution[0])

             


 
# Main program
if __name__ == "__main__":
    # Ukuran Maze
    N = 4

    # Test Case1
    maze = [[1, 1, 1, 1],
            [0, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1] ]
    print("Maze 1:")
    printSolution(maze)
    print()
    start_time = time.time()
    print("Test Case 1")
    solveMaze(maze, N)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    solveWithBF(maze, N)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("============================================")
    print()


    # Test Case2
    maze = [[1, 1, 0, 1],
            [0, 1, 1, 1],
            [0, 0, 1, 0],
            [1, 1, 1, 1]]
    print("Maze 2:")
    printSolution(maze)
    print()
    start_time = time.time()
    print("Test Case 2")
    solveMaze(maze, N)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    solveWithBF(maze, N)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("============================================")
    print()


    # Test Case3
    N = 5
    maze = [[1, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1]]
    print("Maze 3:")
    printSolution(maze)
    print()
    start_time = time.time()
    print("Test Case 3")
    solveMaze(maze, N)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    solveWithBF(maze, N)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("============================================")


    # Test Case4
    N = 5
    maze = [[1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0],
            [1, 1, 1, 1, 1]]
    print("Maze 4:")
    printSolution(maze)
    print()
    start_time = time.time()
    print("Test Case 4")
    solveMaze(maze, N)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    solveWithBF(maze, N)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("============================================")





