import ast
from functools import lru_cache
from math import ceil, log
import re


@lru_cache(maxsize=2048)
def encode(num, depth):
    if num == 0:
        return "_ - _"
    if num <= 5:
        return "_" * num
    return "(" + convert(num, depth + 1) + ")"


@lru_cache(maxsize=2048)
def convert(num, depth=0):
    result = ""
    while num:
        base = shift = 0
        diff = num
        span = int(ceil(log(abs(num), 1.5))) + (16 >> depth)
        for test_base in range(span):
            for test_shift in range(span):
                test_diff = abs(num) - (test_base << test_shift)
                if abs(test_diff) < abs(diff):
                    diff = test_diff
                    base = test_base
                    shift = test_shift
        if result:
            result += "+" if num > 0 else "-"
        elif num < 0:
            base = -base
        if shift == 0:
            result += encode(base, depth)
        else:
            result += "(%s << %s)" % (encode(base, depth), encode(shift, depth))
        num = diff if num > 0 else -diff
    return result


def visit_Call(node: ast.Call):
    if isinstance(node.func, ast.Name):
        if node.func.id == "open":
            return False
    return True


@lru_cache(maxsize=2048)
def leave_Str(node: ast.Str):
    if len(node.s) > 1 and not re.findall(r"\\.", node.s):
        codes = [ord(c) for c in node.s]
        num = sum(codes[i] * 256**i for i in range(len(codes)))
        obfus = convert(num)
        # khá may mắn khi source 2014 lại dùng được ở năm 2024!
        # Source: https://benkurtovic.com/2014/06/01/obfuscating-hello-world.html
        print(obfus)
        decode_func = f'(lambda _, __, ___, ____, _____, ______, _______, ________:\
(lambda _, __, ___: _(_, __, ___))(\
		lambda _, __, ___:\
			bytes([___ % __]) + _(_, __, ___ // __) if ___ else\
			(lambda: _).__code__.co_lnotab,\
		_ << ________,\
		{obfus}\
	)\
)(\
	*(lambda _, __, ___: _(_, __, ___))(\
		(lambda _, __, ___:\
			[__(___[(lambda: _).__code__.co_nlocals])] +\
			_(_, __, ___[(lambda _: _).__code__.co_nlocals:]) if ___ else []\
		),\
		lambda _: _.__code__.co_argcount,\
		(\
			lambda _: _,\
			lambda _, __: _,\
			lambda _, __, ___: _,\
			lambda _, __, ___, ____: _,\
			lambda _, __, ___, ____, _____: _,\
			lambda _, __, ___, ____, _____, ______: _,\
			lambda _, __, ___, ____, _____, ______, _______: _,\
			lambda _, __, ___, ____, _____, ______, _______, ________: _\
		)\
	)\
).decode("utf-8")'
        return ast.parse(decode_func, mode="eval").body
    return node


def fm(node: ast.JoinedStr) -> ast.Call:
    return ast.Call(
        func=ast.Attribute(
            value=ast.Constant(value="{}" * len(node.values)),
            attr="format",
            ctx=ast.Load(),
        ),
        args=[
            value.value if isinstance(value, ast.FormattedValue) else value
            for value in node.values
        ],
        keywords=[],
    )


def obfuscate_string_literals(tree):
    class StringToLambdaTransformer(ast.NodeTransformer):
        def visit_Call(self, node):
            if not visit_Call(node):
                return node
            return self.generic_visit(node)

        def visit_Str(self, node):
            return leave_Str(node)

        def visit_JoinedStr(self, node: ast.JoinedStr):
            return fm(node)

    transformer = StringToLambdaTransformer()
    new_tree = transformer.visit(tree)
    return new_tree


with open("lib.py", "r", encoding="utf-8") as file:
    code = file.read()
tree = ast.parse(code)
obfuscate_string_literals(tree)
code = ast.unparse(tree)
open("167362.py", "w", encoding="utf8").write(str(code))
print(code)
print("#" * 50)
exec(code)
