<div align="center">
    <h1>Interview Coding Questions</h1>
</div>

---

## `1` Overview

This is a web application built with React that contains the coding questions.

## `2` Folder Structure

```
├── react/
├──── public/               - Contains the HTML template and any static assets
├──── src/                  - Contains the source code for the React application
│     └── components/       - React components and their tests used in the application
│     ├── App.tsx           - Core component that manages the logic and user interface
│     ├── main.tsx          - Entry point for rendering the React app into the HTML template
├──── index.html            - Template file which is served up when script is run
├──── .eslintrc             - ESLint configuration for linting code
├──── .prettierrc           - Prettier configuration for code formatting rules
├──── tsconfig.json         - TypeScript configuration for compiler and linting options
├──── package.json          - Configuration file for npm packages and project settings
└── README.md
```

## `3` Running the React Application Locally

Before you begin, ensure you have met the prerequisites, and then
follow these steps to run the application locally.

<details><summary><b>Show instructions</b></summary>

1. **Clone the repository**: Start by cloning the repository to your local machine.
2. **Navigate to the `react` directory**
3. **Install dependencies**: Install the project dependencies using npm.
   ```shell
    npm install
    ```
   Running npm install will ensure that your project has access to the required packages and libraries defined in the
   package.json file.
4. Start the development server:
    ```shell
    npm run dev
    ```
   The `npm run dev` command is defined in "scripts" in `package.json` and starts the development server provided by
   Vite. It automatically compiles and serves the React application.
5. Once the development server starts,
   it will display the actual URL in the terminal. You can access the application by navigating to the URL shown in your
   terminal.

</details>

<details><summary><b>Prerequisites</b></summary>

- Node.js: Make sure you have Node.js installed.
  Node.js includes npm (package manager) by default.  
  To confirm that Node.js is installed correctly, open your terminal or command prompt and run the following commands:
    - ```shell 
      node -v # Displays the current version of Node.js.
      ```
    - ```shell
      npm -v # Displays the current version of npm.
      ```
- An editor or Integrated Development Environment (IDE)
    - Visual Studio Code
    - Visual Studio
    - WebStorm

</details>
