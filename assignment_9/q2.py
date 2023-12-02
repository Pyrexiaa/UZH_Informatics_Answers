import copy
# The signatures of this class and its task methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce grading/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        assert isinstance(authors, list)
        assert isinstance(title, str)
        assert isinstance(year, int)
        self.__authors = authors
        self.__title = title
        self.__year = year

    def get_authors(self):
        return copy.deepcopy(self.__authors)

    def get_title(self):
        return copy.deepcopy(self.__title)

    def get_year(self):
        return copy.deepcopy(self.__year)
    
    def set_authors(self, x):
        self.__authors = x

    def set_title(self, x):
        self.__authors = x

    def set_year(self, x):
        self.__authors = x

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.
    # We've provided a starting point for one of the operators:
    def __le__(self, other): # <=
        if not isinstance(other, Publication):
            return NotImplemented
        
        # Compare authors' lists first
        if self.__authors != other.__authors:
            return self.__authors <= other.__authors
        
        # If authors are identical, compare titles
        if self.__title != other.__title:
            return self.__title <= other.__title
        
        # If titles are also identical, compare years
        return self.__year <= other.__year
    
    def __ge__(self, other): # >=
        if not isinstance(other, Publication):
            return NotImplemented
        
        # Compare authors' lists first
        if self.__authors != other.__authors:
            return self.__authors >= other.__authors
        
        # If authors are identical, compare titles
        if self.__title != other.__title:
            return self.__title >= other.__title
        
        # If titles are also identical, compare years
        return self.__year >= other.__year

    def __lt__(self, other): # <
        if not isinstance(other, Publication):
            return NotImplemented
        
        if self.__authors != other.__authors:
            return self.__authors < other.__authors
        
        if self.__title != other.__title:
            return self.__title < other.__title
        
        return self.__year < other.__year

    def __gt__(self, other): # >
        if not isinstance(other, Publication):
            return NotImplemented
        
        if self.__authors != other.__authors:
            return self.__authors > other.__authors
        
        if self.__title != other.__title:
            return self.__title > other.__title
        
        return self.__year > other.__year

    def __ne__(self, other): # !=
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors, self.__title, self.__year) != (other.__authors, other.__title, other.__year)

    def __eq__(self, other): # ==
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors, self.__title, self.__year) == (other.__authors, other.__title, other.__year)

    def __hash__(self):
        return hash((tuple(self.__authors), self.__title, self.__year))

    def __repr__(self):
        authors_str = "["+', '.join([f'"{author}"' for author in self.__authors])+"]"
        return f'Publication({authors_str}, "{self.__title}", {self.__year})'

    def __str__(self):
        authors_str = "["+', '.join([f'"{author}"' for author in self.__authors])+"]"
        return f'Publication({authors_str}, "{self.__title}", {self.__year})'

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = """Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"""
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    print(p2 < p3) # False
    print(p2 > p3) # False
    print(p2 <= p3)
    print(p2 >= p3)
    print(p2 != p3)

    sales = {
        p1: 273,
        p2: 398,
    }
