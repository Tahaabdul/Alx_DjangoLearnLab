## Retrieve the Book Instance

**Command:**

```python
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year


expected output:
('1984', 'George Orwell', 1949)
```
