from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os



class Post(models.Model):
    COURSE_CHOICES = [
        ('BIM', 'Bachelor in Information Management'),
        ('BCA', 'Bachelor in Computer Application'),
        ('CSIT', 'BSc. Computer Science and Information Technology'),
    ]

    SEMESTER_CHOICES = [
        ('First', 'First Semester'),
        ('Second', 'Second Semester'),
        ('Third', 'Third Semester'),
        ('Fourth', 'Fourth Semester'),
        ('Fifth', 'Fifth Semester'),
        ('Sixth', 'Sixth Semester'),
        ('Seventh', 'Seventh Semester'),
        ('Eighth', 'Eighth Semester'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='Files', null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    # ------------- Meta Info -------------
    class Meta:
        ordering = ['-date_posted']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title} ({self.course} - {self.semester})"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # ------------- Helper Methods -------------

    @property
    def extension(self):
        """Returns lowercase file extension (e.g., '.jpg')."""
        if not self.file:
            return ''
        _, ext = os.path.splitext(self.file.name)
        return ext.lower()

    @property
    def filename(self):
        """Returns just the filename without path."""
        if not self.file:
            return ''
        return os.path.basename(self.file.name)

    @property
    def is_image(self):
        """Check if the file is an image (jpg, jpeg, png)."""
        return self.extension in ['.jpg', '.jpeg', '.png']

    @property
    def is_video(self):
        """Check if the file is a video (mp4)."""
        return self.extension == '.mp4'

    @property
    def is_pdf(self):
        """Check if the file is a PDF."""
        return self.extension == '.pdf'

    @property
    def is_ppt(self):
        """Check if the file is a PowerPoint presentation."""
        return self.extension in ['.ppt', '.pptx']

    @property
    def is_doc(self):
        """Check if the file is a Word document."""
        return self.extension in ['.doc', '.docx']

    @property
    def file_type(self):
        """Returns a readable file type label."""
        if self.is_image:
            return "Image"
        elif self.is_video:
            return "Video"
        elif self.is_pdf:
            return "PDF Document"
        elif self.is_ppt:
            return "PowerPoint Presentation"
        elif self.is_doc:
            return "Word Document"
        elif self.file:
            return "Other File"
        return "No File"
