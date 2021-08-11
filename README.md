# tinykernel
> A minimal Python kernel, so you can run Python in your Python.


All the clever stuff in this library is provided by Python's builtin `ast` module and compilation/exec/eval system, along with [IPython](https://ipython.org/)'s `CachingCompiler` which does some [deep magic](https://cprohm.de/article/better-test-output-with-ast-rewriting-and-a-patched-standard-library.html/). `tinykernel` just brings them together with a little glue.

## Install

With pip:

    pip install tinykernel

With conda:

    conda install -c fastai tinykernel

## How to use

This library provides a single class, `TinyKernel`, which is a tiny persistent kernel for Python code:

```python
k = TinyKernel()
```

Call it, passing Python code, to have the code executed in a separate Python environment:

```python
k("a=1")
```

Expressions return the value of the expression:

```python
k('a')
```




    1



All variables are persisted across calls:

```python
k("a+=1")
k('a')
```




    2



Multi-line inputs are supported. If the last line is an expression, it is returned:

```python
k("""import types
b = SimpleNamespace(foo=a)
b""")
```




    namespace(foo=2)



The original source code is stored, so `inspect.getsource` works and, tracebacks have full details.

```python
k("""def f(): pass # a comment
import inspect
inspect.getsource(f)""")
```




    'def f(): pass # a comment\n'



## Acknowledgements

Thanks to Christopher Prohm, Matthias Bussonnier, and Aaron Meurer for their helpful insights in [this twitter thread](https://twitter.com/jeremyphoward/status/1424990665746763781).
