# Contributing to TraverseCraft

We welcome you to get more involved with the TraverseCraft project! If you are new to contributing, we recommend that you first read our [contributing guide](). If you are contributing code or documentation, please follow our guides for setting up and managing a development environment and workflow. For code, documentation, or triage, please follow the corresponding [contribution guidelines]().

## [Ways to Contribute to TraverseCraft]()

### 1. Optimizing and Refactoring Code
Improve the performance and maintainability of TraverseCraft.

### 2. Detailing Unclear Documentation and Writing New Examples
Enhance documentation clarity and provide comprehensive examples.

### 3. Helping the Community
Engage with TraverseCraft users and contribute to discussions.

### 4. Reporting and Fixing Bugs
Identify and resolve issues to improve TraverseCraft stability.

### 5. Requesting and Implementing New Features
Suggest and add new functionalities to the project.

## [Contribution Types]()

### [Bug Reports]()
Report bugs to help us improve TraverseCraft. Please provide detailed information about the issue and steps to reproduce it.

### [New Feature Requests]()
Suggest new features to enhance TraverseCraft. Provide a clear description and potential use cases.

### [Documentation Updates]()
Help us keep the documentation up-to-date and clear. Report any issues or submit changes directly.

## Setting Up the Environment

### Manually

1. Clone the repository:
   ```bash
   git clone https://github.com/srajan-kiyotaka/TraverseCraft.git
   ```

2. Change the directory to the cloned repository:
    ```bash
    cd TraverseCraft
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

5. Install the dependencies:
    ```bash
    pip install prettytable
    ```

### Using Docker

1. Build the Docker image:
    ```bash
    docker build -t traverse-craft:latest .
    ```

2. Run the Docker container:
    ```bash
    docker run -it --rm traverse-craft:latest
    ```

3. Clone the repository:
   ```bash
   git clone https://github.com/srajan-kiyotaka/TraverseCraft.git
   ```

4. Change the directory to the cloned repository:
    ```bash
    cd TraverseCraft
    ```

5. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

6. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Testing Guidelines

1. **Setting Up the Testing Environment**
   - Ensure all necessary dependencies are installed and the testing framework is configured.

2. **Writing Tests**
   - Create descriptive and comprehensive tests for new features and bug fixes, including edge cases.

3. **Running Tests**
   - Execute the test suite and individual tests to ensure functionality.

4. **Continuous Integration (CI)**
   - Verify that the CI pipeline passes all tests before requesting a review.

5. **Code Coverage**
   - Generate and review code coverage reports to ensure adequate test coverage.

6. **Mocking and Stubbing**
   - Use mocks and stubs to isolate tests from external dependencies.

7. **Best Practices**
   - Write atomic, repeatable tests with clear assertions to maintain code quality.

## Write Documentation

1. **Method or Feature Docstring Update**
   - Whenever a new method or feature is added, ensure that the corresponding docstring is updated. This maintains the readability and reliability of the codebase.

2. **Method or Feature README Update**
   - Whenever a new method or feature is added, ensure that the README of the project is updated. This highlights new features or methods in the project documentation.

3. **Method or Feature Documentation Update**
   - Whenever a new method or feature is added, ensure that the project docs are updated. This ensures that all new updates are properly documented and the project documentation remains current.

4. **Requesting Website Update**
   - Whenever a new method or feature is added, ensure that a request is made to update the project's website with the new feature.

## Pull Request Guidelines

1. **Title and Description**
   - Ensure that the pull request has a clear and concise title, along with a detailed description of the changes being made. This helps reviewers understand the context and purpose of the pull request.

2. **Reference Issues**
   - If the pull request addresses any existing issues, reference them in the description using the appropriate keywords (e.g., "closes #123"). This helps maintain a clear link between the pull request and the issue tracker.

3. **Code Quality**
   - Ensure that the code adheres to the project's coding standards and guidelines. Use consistent formatting, meaningful variable names, and provide comments where necessary to enhance readability.

4. **Testing**
   - Include tests for any new features or bug fixes. Ensure that all existing tests pass before submitting the pull request. This helps maintain the integrity of the codebase.

5. **Documentation**
   - Update any relevant documentation to reflect the changes introduced in the pull request. This includes updating the README, inline documentation, and any other pertinent documentation files.

6. **Peer Reviews**
   - Request reviews from team members or relevant stakeholders. Be responsive to feedback and make necessary adjustments to ensure the quality and accuracy of the pull request.

7. **Merge Conflicts**
   - Check for and resolve any merge conflicts before submitting the pull request. This ensures a smooth integration process and reduces the workload for reviewers.

8. **Continuous Integration**
   - Ensure that the pull request passes all continuous integration (CI) checks. Address any CI failures promptly to maintain the stability and reliability of the codebase.

## Community and Discussion

- **Community Engagement**
  - We encourage all community members to engage actively in discussions, provide feedback, and support fellow contributors and users.

- **Discussion**
  - Join our [Discussions](LINK_TO_DISCUSSIONS_PAGE) page to ask questions, share ideas, and stay updated on project announcements.

- **Announcements**
  - Important project updates, releases, and news are shared on our Discussions page. Stay informed and participate in discussions.

- **Feedback**
  - Your feedback is valuable to us. Share your thoughts and suggestions on how we can improve TraverseCraft.

- **Contribution**
  - Your contributions are what make TraverseCraft great! Whether it's code, documentation, or community engagement, every contribution is appreciated.

## Contribute

For more information on how to contribute to TraverseCraft, please see the following sections:

- **[Contributing Guidelines](LINK_TO_CONTRIBUTING_GUIDELINES)**
- **[Setting Up for Development](LINK_TO_SETUP_GUIDE)**
- **[Testing Guidelines](LINK_TO_TESTING_GUIDELINES)**
- **[Write Documentation](LINK_TO_DOCUMENTATION_GUIDE)**
- **[Pull Request Guidelines](LINK_TO_PULL_REQUEST_GUIDELINES)**
