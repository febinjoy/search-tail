# Search-Tail

Search-Tail (`stail`) is a command-line tool similar to `tail`, with added search functionality and keyword highlighting.

## Features

- Displays the last `n` lines of a file (default: 50).
- Highlight search term matches in green.
- Predefined keywords like "ERROR", "CRITICAL", "WARNING", etc., are also highlighted.
  - This could be configured to suit your needs.
- Navigate through matches using `n` (next) and `p` (previous).
- Reload file to view newly added lines with `r`.
- Search for another keyword with `s`.
- Quit with `q`.

## Installation

### Using `install.sh`

1. Clone the repository:

   ```bash
   git clone https://github.com/febinjoy/search-tail.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd search-tail
   ```

3. Make the `install.sh` script executable:

   ```bash
   chmod +x install.sh
   ```

4. Run the `install.sh` script:

   ```bash
   ./install.sh
   ```

### Manual Steps

You can also manually add the alias to your `.bashrc` or `.zshrc`

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Add the following alias to your `.bashrc` or `.zshrc`:

   ```bash
   alias stail='python3 <Path of Search-Tail>/search_tail/__main__.py "$@"'
   ```

3. Source your `.bashrc` or `.zshrc` file:

   ```bash
   source ~/.bashrc
   ```

   or

   ```bash
   source ~/.zshrc
   ```

## Usage

```bash
stail <file_name> [-n <number_of_lines>] [-s <search_term>]
```

- `<file_name>`: The name of the file to display.
- `-n <number_of_lines>`: Display the last n lines of the file (default: 50).
- `-s <search_term>`: Search for the specified term and highlight matches.

## Navigation Commands

- `n`: Go to the next match.
- `p`: Go to the previous match.
- `r`: Reload the file to view newly added lines.
- `s`: Search for another keyword.
- `q`: Quit.

## Example

```bash
stail -n 100 -s deleted my_log_file.log
```

This command displays the last 100 lines of `my_log_file.log` and highlights occurrences of the word `deleted` along with predefined keywords like "ERROR", "CRITICAL", "WARNING" etc.
