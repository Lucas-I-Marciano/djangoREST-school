# Django REST School API

## Project Overview
This project is an API based on a school business model, developed using Django REST Framework. It follows best practices by starting the project with a `setup` directory and organizing apps in a separate `apps` folder.

<img src="https://github.com/user-attachments/assets/bc7946cf-6ec2-4a61-b90e-68d0b152fdf9" alt="Girl in a jacket" width="350" height="300">
<img src="https://github.com/user-attachments/assets/330374c8-28f3-43b0-a257-13e108aa4d7d" alt="Girl in a jacket" width="550" height="300">
<img src="https://github.com/user-attachments/assets/2a6be270-c181-4ee5-9d4d-02bacd78d53f" alt="Girl in a jacket" width="904" height="300">





## Project Structure
- **setup**: Contains project configuration files.
- **apps**: Contains the individual apps for the project, which are `snippets` and `school`.

## Apps

### Snippets
The `snippets` app was created to follow the Django REST Framework tutorial and explore the framework's capabilities. It includes the `Snippet` model, which stores code snippets with fields such as `owner`, `created`, `title`, `code`, `linenos`, `language`, `style`, and `highlighted`.

#### Model
```python
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_snippets')
    highlighted = models.TextField()

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter) # HTML string
        super().save(*args, **kwargs)
```

#### Permissions
Custom permission to allow only the owner of a snippet to edit it:
```python
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS:  ('GET', 'HEAD', 'OPTIONS')
            return True
        
        if request.user == obj.owner : # obj:  Snippet object (i) => i=instance
            return True
```


### School
The `school` app includes models for students, courses, and enrollments. It uses serializers to display enrollments by students and courses, and implements global permissions and throttling to manage API access.

#### Models
- **Student**: Fields to identify each student.
- **Course**: Fields to describe each course.
- **Enrollment**: Creates a unique record for a student enrolled in a specific course.

#### Serializers
Custom serializers to display enrollments by course and by student, and handle specific fields:
```python
class MatriculasEstudantesSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta :
        model = Matricula
        fields = ['id', 'curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
```

#### Throttle
It has a limit of request by minute a user can make

#### Serializer Version
It apply DEFAULT_VERSIONING_CLASS to handle with two version of serializer for the same view by using 
```python 
def get_serializer_class(self):
```

## How to Use
1. Clone the repository: `git clone https://github.com/Lucas-I-Marciano/djangoREST-school`
2. Navigate to the project directory: `cd djangoREST-school`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the development server: `python manage.py runserver`
9. Access the API at `http://127.0.0.1:8000/`


## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please contact [Lucas I Marciano](https://github.com/Lucas-I-Marciano)
