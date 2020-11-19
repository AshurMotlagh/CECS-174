class Member:
    total_mem = 0  # creating a counter for the number of members.
    bks_out = []  # creating a list for the books that are checked out.
    videos_out = []  # creating a list for the videos being checked out.

    def __init__(self, name):
        self.name = name
        self.list_media_of_mem = []  # member's personal list of checked out items.
        Member.total_mem += 1  # add to member count.

    def checkout(self, item):
        if len(self.list_media_of_mem) < 2:  # condition to make sure the member cant checkout more than two books.

            if item.check_out is False and isinstance(item, Book):  # making sure that the book hasn't been checked out.
                self.list_media_of_mem.append(item)  # gives ownership of book to member.
                self.bks_out.append(item)  # add book name to the list of books checked out.
                item.check_out = True  # book is now checked out.
                item.owner = self.name  # keeping record of current owner.
                print(self.name, "has checked out:", item, "\n")

            elif item.check_out is False and isinstance(item, Video):  # making sure that the video hasn't checked out.
                self.list_media_of_mem.append(item)  # giver ownership of video to member.
                self.videos_out.append(item)  # add book name to the list of books checked out.
                item.check_out = True  # video is now checked out.
                item.owner = self.name  # keeping record of current owner.
                print(self.name, "has checked out:", item, "\n")

            else:  # telling member that someone else has the item.
                print("Sorry", self.name, ",", item, "is not available, checked out by", item.owner, "\n")

        else:  # you cant checkout more than 2 books.
            print(self.name, "reached the maximum number (2) of borrowed items, so can't check out:", item, "\n")

    def checkin(self, item):
        if item not in self.list_media_of_mem:  # to fix logic error of checking in a item that hasn't been checked out.
            print("Can't Check in item that was not checked out at first \n")

        elif isinstance(item, Book):
            self.list_media_of_mem.remove(item)  # removing book from list of what member checked out.
            self.bks_out.remove(item)  # removing the book from checkout list / checking in the book.
            item.check_out = False  # book is now checked in.
            item.owner = " "  # clearing the owner name.
            print(self.name, "checked in: ", item, "\n")

        else:
            self.list_media_of_mem.remove(item)  # removing video from list of what member checked out.
            self.videos_out.remove(item)  # removing the video from checkout list / checking in the video.
            item.check_out = False  # video is now checked in.
            item.owner = " "  # clearing the owner name.
            print(self.name, "checked in: ", item, "\n")

    def printCheckedOutItems(self):
        print("Items checked out by", self.name, "\n")
        for item in self.list_media_of_mem:  # printing the checked out items of each member using polymorphism.
            print("\t", item, "\n")


class Media:  # this is the superclass.
    total_bks = 0  # counter for keeping track of total number of books.
    total_videos = 0  # counter for keeping track of total number of videos.

    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.check_out = False
        self.owner = " "


class Book(Media):  # making Media the superclass.
    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)  # calling from the super.
        self._num_pages = num_pages
        Media.total_bks += 1  # adds to book count.

    def __repr__(self):
        return "Book--> " + self.title + " written by " + self.author


class Video(Media):  # making Media the superclass.
    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher)  # calling from the super.
        self._rum_time = str(run_time)
        Media.total_videos += 1  # add to video count.

    def __repr__(self):
        return "Video--> " + self._rum_time + " mins video " + self.title + " created by " + self.author


def displayStats():
    print("\n", "*" * 42, "\n")  # line separation.
    print("Record of Library:\n")
    print("Total number of Books = ", Media.total_bks, "\n")  # total number of books.
    print("Numbers of books checked out = ", len(Member.bks_out), "\n")  # how many books checked out.
    print("Total number of videos = ", Media.total_videos, "\n")  # total number of videos.
    print("Numbers of videos checked out = ", len(Member.videos_out), "\n")  # how many videos checked out.
    print("Total number of members = ", Member.total_mem)  # total number of members.
    print("\n", "*" * 70, "\n")
    print("The following items are checked out of the library:\n ")
    for book_left in Member.bks_out:  # telling us what books are checked out & what member has them using polymorphism.
        print(book_left, "checked out by", book_left.owner, "\n")
    for vid_left in Member.videos_out:  # printing what videos are checked out & what member has them using polymorphism
        print(vid_left, "checked out by", vid_left.owner, "\n")


book1 = Book("Python for Beginners", "Unknown", "CBS", "40")
book2 = Book("Python for Kids", "Jason R. Briggs", "NBC", "23")
video1 = Video("Tom and Jerry", "W.Hannah, J.Barbara", "PBS", "30")
video2 = Video("Rick and Morty", "Billy", "FOX", "62")
video3 = Video("Rick", "Billy", "FOX", "62")
video4 = Video("Morty", "Billy", "FOX", "62")
video5 = Video("Ashur", "MOthrt", "FOX", "35")

Joe = Member("Joe Smith")
Jim = Member("Jim Stuart")
Ashur = Member("Ashur Motlagh")
Gabby = Member("Gabby Kim")
Joe.checkout(book1)
Joe.checkin(book2)
Joe.checkin(book2)
Joe.checkin(book2)
Joe.checkin(video2)
Joe.checkin(book2)
Joe.checkout(book2)
Joe.checkout(video1)
Joe.checkin(book1)
Jim.checkout(book2)
Joe.checkin(book2)
Jim.checkout(video1)
Jim.checkout(book1)
Joe.checkout(video2)
Ashur.checkout(book1)
Ashur.checkout(book2)
Ashur.checkout(video1)
Ashur.checkout(video2)
Ashur.checkout(video3)
Ashur.checkout(video4)
Gabby.checkout(video4)
Gabby.checkout(video5)
Joe.printCheckedOutItems()
Jim.printCheckedOutItems()
Ashur.printCheckedOutItems()
Gabby.printCheckedOutItems()

displayStats()
