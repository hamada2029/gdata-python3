#!/usr/bin/python


__author__ = "James Sams <sams.james@gmail.com>"


import unittest
from gdata import test_data
import gdata.books
import atom


class BookEntryTest(unittest.TestCase):

    def testBookEntryFromString(self):
        entry = gdata.books.Book.FromString(test_data.BOOK_ENTRY)
        self.assertTrue(isinstance(entry, gdata.books.Book))
        self.assertEqual([x.text for x in entry.creator], ['John Rawls'])
        self.assertEqual(entry.date.text, '1999')
        self.assertEqual(entry.format.text, '538 pages')
        self.assertEqual([x.text for x in entry.identifier],                   
           ['b7GZr5Btp30C', 'ISBN:0198250541', 'ISBN:9780198250548'])
        self.assertEqual([x.text for x in entry.publisher],
            ['Oxford University Press'])
        self.assertEqual(entry.subject, None)
        self.assertEqual([x.text for x in entry.dc_title],
            ['A theory of justice'])
        self.assertEqual(entry.viewability.value,
            'http://schemas.google.com/books/2008#view_partial')
        self.assertEqual(entry.embeddability.value,
            'http://schemas.google.com/books/2008#embeddable')
        self.assertEqual(entry.review, None)
        self.assertEqual([getattr(entry.rating, x) for x in
            ("min", "max", "average", "value")], ['1', '5', '4.00', None])
        self.assertEqual(entry.GetThumbnailLink().href,
            'http://bks0.books.google.com/books?id=b7GZr5Btp30C&printsec=frontcover&img=1&zoom=5&sig=ACfU3U121bWZsbjBfVwVRSK2o982jJTd1w&source=gbs_gdata')
        self.assertEqual(entry.GetInfoLink().href,
            'http://books.google.com/books?id=b7GZr5Btp30C&ie=ISO-8859-1&source=gbs_gdata')
        self.assertEqual(entry.GetPreviewLink(), None)
        self.assertEqual(entry.GetAnnotationLink().href,
            'http://www.google.com/books/feeds/users/me/volumes')
        self.assertEqual(entry.get_google_id(), 'b7GZr5Btp30C')

    def testBookFeedFromString(self):
        feed = gdata.books.BookFeed.FromString(test_data.BOOK_FEED)
        self.assertTrue(isinstance(feed, gdata.books.BookFeed))
        self.assertEqual( len(feed.entry), 1)
        self.assertTrue(isinstance(feed.entry[0], gdata.books.Book))

    def testBookEntryToDict(self):
        book = gdata.books.Book()
        book.dc_title.append(gdata.books.Title(text='a'))
        book.dc_title.append(gdata.books.Title(text='b'))
        book.dc_title.append(gdata.books.Title(text='c'))
        self.assertEqual(book.to_dict()['title'], 'a b c')

if __name__ == "__main__":
    unittest.main()
