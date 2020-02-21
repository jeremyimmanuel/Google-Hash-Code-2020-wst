from book import Book

class Library:
    """
    lid: library id
    books: set of books
    sign_up_time: intuitive
    ship_rate: intuitive
    """
    def __init__(self, lid: int, books: list, sign_up_time: int, ship_rate: int):
        self.lid = lid
        self.books = books
        self.sign_up_time = sign_up_time
        self.ship_rate = ship_rate
        self.books_scanned = 0
        self.books_order = []
    
    def add_book(self, book):
        self.books.append(book)

    def ship_book(self, has_shipped: set):
        # print('Im in shipbook')
        # print('ship_rate : %d' % self.ship_rate)
        i = 0
        shipCount = 0
        bookScore = 0
        while shipCount < self.ship_rate:
            if (i >= len(self.books)):
                break
                

            if(self.books[i] not in has_shipped):
                has_shipped.add(self.books[i])
                bookScore += self.books[i].score
                shipCount += 1
                self.books_order.append(self.books[i])
            i += 1

        self.books_scanned = shipCount
        return bookScore

    def sort_my_face(self):
        self.books = sorted(self.books, reverse=True)

    # def __repr__(self):
    #     return '''
    #     library {
    #         id : %d,
    #         sign_up_time : %d,
    #         ship_rate : %d,
    #         books : %s,
    #     }
    #     ''' % (self.lid, self.sign_up_time, self.ship_rate, self.books)