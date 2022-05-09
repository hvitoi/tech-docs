# App

## Relationships

- **One** `instructor` has **One** `instructor_detail`
- **One** `instructor` has **Many** `course`

## Cascading

- If deleting a course, don't delete the instructor
- If deleting an instructor, don't delete the courses
