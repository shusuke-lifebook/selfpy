try:
    data = 5 / 0
except Exception:
    print("Exception")
except ArithmeticError:  # type: ignore
    print("ArithmeticError")
except OverflowError:  # type: ignore
    print("OverflowError")
