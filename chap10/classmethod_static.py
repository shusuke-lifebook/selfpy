class Area:
    @staticmethod
    def circle(radius: float | int) -> float | int:
        return radius * radius * 3.14


if __name__ == "__main__":
    print(Area.circle(10))
