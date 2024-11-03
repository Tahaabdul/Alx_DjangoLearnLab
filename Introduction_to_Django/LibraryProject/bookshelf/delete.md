## Delete the Book Instance

**Command:**

```
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

```

**expected output:**

```
<QuerySet []>
```
