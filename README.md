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

### When search keyword is not provided.

```bash
stail -n 100 -my_log_file.log
```
This displays the last 100 lines of `my_log_file.log`. Since we have not specified any search keyword, only the predefined keywords like "ERROR", "CRITICAL", "WARNING" etc are highlighted in respective colors.

![image](https://github.com/user-attachments/assets/0814e250-974c-4245-9f77-640a72c80563)


### When search keyword is provided.

```bash
stail -n 100 -s database my_log_file.log
```

This displays the last 100 lines of `my_log_file.log` and highlights occurrences of the word `database` along with predefined keywords like "ERROR", "CRITICAL", "WARNING" etc in their respective colors. Current search position is highlighed with a background color. Pressing `n` for next and `p` for previous will help navigation.

![image](https://github.com/user-attachments/assets/e3c557cd-651e-433c-8912-ba4f34ea35f8)

### Search once log is displayed

At any point, press `s` to perform a search. You will be prompted to enter a search keyword. It will work the same way as providing the ssearch keyword with `-s` argument.

![image](https://github.com/user-attachments/assets/5dec900d-9f5b-4079-943e-459d61e9179b)
