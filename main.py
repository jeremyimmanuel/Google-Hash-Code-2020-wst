#from __future__ import braces
from book import Book
from library import Library
import sys

scores = []
libraries = []
has_shipped = set()
signedUp = []
totalBooks = -1
totalLibs = -1
totalDays = -1

def parseInput(fileName):
    
    f = open(fileName, "r")
    #contents = f.read()
    #print(contents)
    #lines = f.readlines()
    
    libCount = 0
    for index,line in enumerate(f):
        if index == 0:
            # number of stuff
            arr = line.strip().split(' ')
            global totalBooks 
            totalBooks = int(arr[0])
            global totalLibs 
            totalLibs = int(arr[1])
            global totalDays 
            totalDays = int(arr[2])
            
        elif index == 1:
            # scores of books
            global scores
            scores = [int(x) for x in line.strip().split(' ')] #reusing arr
 
        elif index % 2 == 0:
            # library lines
            # print('library line : %s' % line)
            # self, lid: int, books: set, sign_up_time: int, ship_rate: int):
            arr = line.strip().split(' ')
            if (len(arr) == 1):
                break
            libInfo = [int(x) for x in arr]
            lib = Library(libCount, [], libInfo[1], libInfo[2])
            libraries.append(lib)
            libCount += 1

        else:
            #book index
            bookInfo = [int(x) for x in line.strip().split(' ')] #reusing arr
            for index_idx,book_idx in enumerate(bookInfo):
                book = Book(book_idx, scores[book_idx])
                libraries[-1].add_book(book)

        #print(index + ": " + line)
    f.close()

def signUp(library):
    # print('signing up a library: {}...'.format(library))
    global signedUp
    signedUp.append(library)
    return library.sign_up_time

# def shipBook(book):
#     print('shipping and scanning a book: {}...'.format(book))
#     has_shipped.add(book)

def main():
    # print(1, 2, 3, 4, 5, sep="😺",end="😾\n")
    #print(scores)
    # parseInput('a_example.txt')
    # parseInput('e_so_many_books.txt')
    parseInput('d_tough_choices.txt')
    [x.sort_my_face() for x in libraries]

    # print('total books : %d' % totalBooks)
    # print('total libs : %d' % totalLibs)
    # print('total days : %d' % totalDays)
    # print('libraries {}'.format(libraries))
    # print('score array : %s' % scores)

   # activeSignup = false #maybe a global?
    scannedScore = 0
    currWaitTime = 0
    lindex = 0
    global has_shipped
    global signedUp

    for i in range(totalDays):
        # print('today is day: ' + str(i))
        if currWaitTime == 0: # sign up a new lib and scan any book from signed up libs
            # assuming Librar
#passies are sorted by priority
            currWaitTime = signUp(libraries[lindex]) # currWaitTime is negative
            lindex += 1
            #scan books
            for su in signedUp: 
                # scan books 
                scannedScore += su.ship_book(has_shipped)

        else: # scan any book from signed up libs
            for su in signedUp: 
                # scan books 
                scannedScore += su.ship_book(has_shipped)
        currWaitTime -= 1

    print('total: %d' % scannedScore)

def writeOutput():
    global totalLibs
    global libraries
    global signedUp

    f = open('e_submissions.txt', 'w')
    f.write(str(totalLibs) + '\n')
    for s in signedUp:
        f.write(str(s.lid) + ' ')
        f.write(str(s.books_scanned) + '\n')
        for i in range(len(s.books_order)):
            f.write(str(s.books_order[i]) + ' ')
        f.write('\n')
        
    f.close() 

if __name__ == '__main__':
    main()
    # writeOutput()