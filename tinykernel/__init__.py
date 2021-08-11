__version__ = "0.0.1"
__all__ = ['TinyKernel']

from ast import parse,Expr,Expression,Module
from .compilerop import CachingCompiler

compiler = CachingCompiler()

class TinyKernel:
    "A tiny persistent kernel for Python code"
    def __init__(self, name='kernel', glb=None): self.name,self.idx,self.glb = name,-1,glb or {}
    def _run(self, p, nm, mode='exec'): return eval(compiler(p, nm, mode), self.glb)

    def __call__(self, code):
        nm = compiler.cache(code, self.idx)
        self.idx += 1
        p = parse(code, filename=nm) if not isinstance(code, Module) else code
        expr = p.body.pop() if p.body and isinstance(p.body[-1], Expr) else None
        self._run(p, nm)
        if expr: return self._run(Expression(expr.value), nm, 'eval')

