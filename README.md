# Text Analyzer

Text Analyzer is a Django project that provides various text analysis features. It allows users to analyze and manipulate text in different ways. The main features include:

- **Remove Punctuations**: Removes punctuations from the input text.
- **Uppercase**: Converts the text to uppercase.
- **Lowercase**: Converts the text to lowercase.
- **Remove Newlines**: Removes newlines from the text.
- **Remove Extra Spaces**: Removes extra spaces from the text.
- **Remove Numbers**: Removes numbers from the text.
- **Reverse Text**: Reverses the order of characters in the text.

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/your-username/text-analyzer.git
   ```

2. Navigate to the project directory:

   ```shell
   cd text-analyzer
   ```

3. Create a virtual environment:

   ```shell
   python -m venv env
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```shell
     source env/bin/activate
     ```

   - On Windows:

     ```shell
     env\Scripts\activate
     ```

5. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Run the Django development server:

   ```shell
   python manage.py runserver
   ```

   The development server will start running at `http://localhost:8000`.

## Usage

1. Open a web browser and navigate to `http://localhost:8000` to access the application.

2. Enter the text you want to analyze in the provided input field.

3. Select the desired text analysis options using the checkboxes.

4. Click the "Analyze" button to perform the selected operations on the input text.

5. The analyzed text and the applied operations will be displayed on the result page.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository.

1. Fork the repository.

2. Create a new branch:

   ```shell
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```shell
   git commit -m "Add your commit message"
   ```

4. Push your changes to your forked repository:

   ```shell
   git push origin feature/your-feature-name
   ```

5. Open a pull request on the GitHub repository to submit your changes for review.

## License

[MIT License](LICENSE)