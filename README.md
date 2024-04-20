# Measurement Scaling Tool

## Overview

This Python program is designed to scale manual measurements taken from a set of points and calculate their scaled values based on a provided scaling factor. It also ensures the consistency of the scaling by verifying that the sum of the scaled measurements matches the original sum of the measurements within a defined tolerance.

## Features

- **Scaling**: The program scales manual measurements based on a given scaling factor.
- **Consistency Check**: It verifies that the sum of the scaled measurements matches the original sum of the measurements within a defined tolerance.
- **Input Flexibility**: Manual measurements can be provided in any format that the `get_manual_measurements()` function can handle.
- **Output Formatting**: The program outputs the scaled measurements in a human-readable format.

## Usage

1. **Input Manual Measurements**:
    - Define manual measurements in the `manual_measurements` module.
    - The measurements should be in the format: `[(label, numerator_ratio, points), ...]`.
        - `label`: A string label for the measurement.
        - `numerator_ratio`: Numerator value for calculating the ratio.
        - `points`: List of points for the measurement.
        
    Example:
    ```python
    horizontal_measurements = [
        ("Measurement 1", 10, [0, 2, 4, 6]),
        ("Measurement 2", 20, [6, 10, 12, 16]),
        # Add more measurements as needed
    ]
    ```

2. **Set Configuration Parameters**:
    - Modify the configuration parameters in the main script as needed:
        - `DISTANCE_PRECISION`: Number of decimal places for distances.
        - `SUM_PRECISION`: Number of decimal places for sum calculations.
        - `SCALING_PRECISION`: Number of decimal places for scaled values.
        - `TOLERANCE`: Tolerance level for sum consistency check.
        - `SCALE_FACTOR`: Scaling factor to apply to the measurements.

3. **Run the Program**:
    ``` sh
    python3 measure_scaling.py
    ```

4. **Review Output**:
    - The output will display the scaled measurements along with the original measurements and scaled values.
    - It will also show the sum of original measurements and the sum of scaled values, verifying their consistency.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
