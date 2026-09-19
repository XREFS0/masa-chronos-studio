# MASA Chronos Studio

A multi-functional timekeeping system incorporating a continuous atomic-style digital clock and a centisecond precision chronometer.

## Technical Architecture

The codebase follows modular software engineering patterns and OOP structure, designed for reliability, high maintainability, and clean separation of concerns:

- **Component Layering**: User interface and computational state are decoupled into specialized controllers and event loops.
- **Defensive Engineering**: Comprehensive validation guards protect against malformed inputs and runtime exceptions.
- **Modern Design Tokens**: Designed with a high-contrast dark aesthetic adhering to modern developer tooling visual standards.


## Preview

![Application Interface](screenshots/app_interface.png)
## Features

- Non-blocking background loop refreshing time and date strings every 50ms.
- Interactive digital stopwatch supporting start, pause, resume, and reset cycles.
- Full localized date formatting and uppercase weekday visualization.
- High-contrast digital display optimized for developer desktop monitors.

## Prerequisites

- Python 3.10 or higher
- Required packages:

```bash
pip install customtkinter
```

## Execution

Initialize and run the module via the command line:

```bash
python "Simple Live Clock App using Tkinter in Python/index.py"
```

## Project Structure

```
.
â”œâ”€â”€ Simple Live Clock App using Tkinter in Python
â”œâ”€â”€ LICENSE             # MIT License
â””â”€â”€ README.md           # Developer documentation
```

## License

This project is licensed under the terms of the MIT License. Refer to the `LICENSE` file for details.

