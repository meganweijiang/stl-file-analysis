# stl-file-analysis

## How to Run

Make sure you have Python >= 3.4 installed
To run the project, from the root directory run:

```
python main.py ./input/SimplePart.stl
```

You may also try with the `Moon.stl` file in the `input` folder, or your own valid `.stl` file
To run the tests, from the root directory run:

```
python -m unittest tests/test.py
```

## Design Explanation

- The individual components of the triangles were very clear classes, hence the creation of the `Vertex`, `Edge`, and `Triangle` classes
- The `fileinput` module was used to simplify file reading, and allowed for easy interchanging between files
- The STL file segments followed a clear pattern, so certain lines provided distinction between the end of a triangle vs. the next triangle
- Heron's formula was used for the area calculations
- I wanted to use some of the functional features of Python, such as `lambda` and `filter` functions

## Potential Improvements

- For millions of triangles, parallelizing the line-processing or reading the input file in segments would help with performance
- This project was written assuming the input is a valid STL file, but error handling could be implemented for if this is not the case
- If the project were to scale, the tests can be split into multiple suites and the `PyTest` framework may be a better option
