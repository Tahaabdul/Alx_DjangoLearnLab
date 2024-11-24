## Create a Book Instance

**Command:**

```
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

**expected output:**

```
<Book: 1984>
```

## Retrieve the Book Instance

**Command:**

```python
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year


expected output:
('1984', 'George Orwell', 1949)
```

## Update the Book Title

**Command:**

```
book.title = "Nineteen Eighty-Four"
book.save()
book.title
```

**expected output:**

```
'Nineteen Eighty-Four'
```

## Delete the Book Instance

**Command:**

```
book.delete()
Book.objects.all()
```

**expected output:**

```
<QuerySet []>
```
