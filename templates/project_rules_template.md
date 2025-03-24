## Starting the project
1. If `dev/project_description.md` empty, you should generate a project description file according to the user input.
2. If `dev/todo.md` empty, you should generate a todo file with planning tasks to complete the project.
3. All listed files inside `dev` directory are created empty file by default, you do not need to check their existance, only generate contents.

## Project documentation
1. `dev/project_description.md` is the project description file of this project, you should go over it for project background information.
2. Please check `dev/todo.md` for the remaining tasks to be completed, and keep updating it every time you finish a task or add a new task.
3. Please update your progress in `dev/progress.md`.

## Code style requirements
1. Writing clear readable code that is compliant with a common style guide.
2. Providing appropriate documentation that is compatible with auto-documentation tools.
3. The project must be well structured (sensible folder structure, README.md, licence etc.) following standard best practice.
4. Uses appropriate version control best practices.
5. When implementing, please check `dev/code_docs.md` for the API documentation of the implemented modules in the project, to see if any function is already implemented and do not implement it again.

## Sustaining the project
1. After you finish the implementation of a module, please summarize only the key function that can be used by other modules into `dev/code_docs.md`.
2. For code files (including .html, .css, .js, .py, etc.), you should keep the length of the file within **400 LINES**. If the file is too long, you should split it into multiple files.
3. When implement everything, please follow the **API FUNCTION DESIGN MODE** that can be re-used for other modules instead of the very tedious `main()` function that cannot be re-used.